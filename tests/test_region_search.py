import requests
import unittest
from .config import BASE_URL

class TestRegionSearch(unittest.TestCase):

    def test_successful_region_search(self):
        # Тест успешной фильтрации по названию региона
        response = requests.get(f"{BASE_URL}?q=Новосибирск")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertTrue(any(item['name'] == 'Новосибирск' for item in data['items']), "Регион 'Новосибирск' не найден в ответе")

    def test_error_for_empty_region_name(self):
        # Тест проверки ошибки при пустом вводе названия региона
        response = requests.get(f"{BASE_URL}?q=")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")

    def test_region_name_3_characters(self):
        # Тест проверки ввода 3 символов в название региона
        response = requests.get(f"{BASE_URL}?q=Нов")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertGreater(len(data['items']), 0, "Регионы не найдены при вводе 3 символов в название региона")
        self.assertTrue(any('Нов' in item['name'] for item in data['items']), "Нет совпадений с введенными символами 'Нов'")

    def test_region_name_4_characters(self):
        # Тест проверки ввода 4 символов в название региона
        response = requests.get(f"{BASE_URL}?q=Ново")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertGreater(len(data['items']), 0, "Регионы не найдены при вводе 4 символов в название региона")
        self.assertTrue(any('Ново' in item['name'] for item in data['items']), "Нет совпадений с введенными символами 'Ново'")

    def test_error_for_2_characters_in_region_name(self):
        # Тест проверки ошибки при вводе 2 символов в название региона
        response = requests.get(f"{BASE_URL}?q=Но")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")

    def test_no_match_for_numeric_region_name(self):
        # Система не находит совпадения при вводе числовых символов в названии региона
        response = requests.get(f"{BASE_URL}?q=123")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertEqual(data['items'], [], "Параметр 'items' должен быть пустым списком при вводе числовых символов в название региона")

    def test_no_match_for_latin_region_name(self):
        # Система не находит совпадения при вводе латинских букв в названии региона
        response = requests.get(f"{BASE_URL}?q=Novosibirsk")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertEqual(data['items'], [], "Параметр 'items' должен быть пустым списком при вводе латинских букв в название региона")

    def test_no_match_for_special_characters_in_region_name(self):
        # Система не находит совпадения при вводе спецсимволов в названии региона
        response = requests.get(f"{BASE_URL}?q=@%№")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertEqual(data['items'], [], "Параметр 'items' должен быть пустым списком при вводе спецсимволов в название региона")

    def test_successful_search_with_russian_and_hyphen(self):
        # Тест успешного поиска региона с русскими буквами и тире
        response = requests.get(f"{BASE_URL}?q=Санкт-Петербург")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertTrue(any(item['name'] == 'Санкт-Петербург' for item in data['items']), "Регион 'Санкт-Петербург' не найден в ответе")

    def test_successful_search_with_cyrillic_yo(self):
        # Тест успешного поиска региона с буквой "ё" в названии
        response = requests.get(f"{BASE_URL}?q=Орёл")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertTrue(any(item['name'] == 'Орёл' for item in data['items']), "Регион 'Орёл' не найден в ответе")

    def test_successful_search_with_space(self):
        # Тест успешного поиска региона с пробелом между словами в названии
        response = requests.get(f"{BASE_URL}?q=Нижний Новгород")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertTrue(any(item['name'] == 'Нижний Новгород' for item in data['items']), "Регион 'Нижний Новгород' не найден в ответе")

if __name__ == '__main__':
    unittest.main()
