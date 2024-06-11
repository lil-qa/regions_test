import requests
import unittest
from .config import BASE_URL

class TestCountryCode(unittest.TestCase):
    def test_filter_by_country_code_ru(self):
        # Тест проверки фильтрации по коду страны "ru"
        response = requests.get(f"{BASE_URL}?country_code=ru")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        for item in data['items']:
            self.assertEqual(item['country']['code'], 'ru', f"Найден элемент, не соответствующий коду страны 'ru': {item}")

    def test_filter_by_country_code_kg(self):
        # Тест проверки фильтрации по коду страны "kg" (Кыргызстан)
        response = requests.get(f"{BASE_URL}?country_code=kg")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        for item in data['items']:
            self.assertEqual(item['country']['code'], 'kg', f"Найден элемент, не соответствующий коду страны 'kg': {item}")

    def test_filter_by_country_code_kz(self):
        # Тест проверки фильтрации по коду страны "kz" (Казахстан)
        response = requests.get(f"{BASE_URL}?country_code=kz")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        for item in data['items']:
            self.assertEqual(item['country']['code'], 'kz', f"Найден элемент, не соответствующий коду страны 'kz': {item}")

    def test_filter_by_country_code_cz(self):
        # Тест проверки фильтрации по коду страны "cz" (Чехия)
        response = requests.get(f"{BASE_URL}?country_code=cz")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        for item in data['items']:
            self.assertEqual(item['country']['code'], 'cz', f"Найден элемент, не соответствующий коду страны 'cz': {item}")

    def test_error_for_empty_country_code(self):
        # Тест проверки ошибки при незаполненном коде страны для фильтрации
        response = requests.get(f"{BASE_URL}?country_code=")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")

    def test_default_country_code(self):
        # Тест проверки, что по умолчанию отображаются города из всех стран
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        self.assertGreater(len(data['items']), 0, "Должны отображаться регионы из всех стран по умолчанию")

    def test_error_for_invalid_country_code(self):
        # Тест проверки ошибки при вводе значений не из списка требований в код страны
        response = requests.get(f"{BASE_URL}?country_code=invalid")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")

if __name__ == '__main__':
    unittest.main()
