import requests
import unittest
from .config import BASE_URL

class TestPagination(unittest.TestCase):

    def test_page_number_1(self):
        # Тест ввода значения "1" в порядковый номер страницы
        response = requests.get(f"{BASE_URL}?page=1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")

    def test_page_number_2(self):
        # Тест ввода значения "2" в порядковый номер страницы
        response = requests.get(f"{BASE_URL}?page=2")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")

    def test_default_page_number(self):
        # Тест значения "1" по умолчанию в порядковом номере страницы
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data)
        self.assertIsInstance(data['items'], list)
        self.assertGreater(len(data['items']), 0, "Должны отображаться элементы на первой странице по умолчанию")

    def test_error_for_alphabetic_page_number(self):
        # Тест проверки ошибки при вводе букв в порядковый номер страницы
        response = requests.get(f"{BASE_URL}?page=one")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")

if __name__ == '__main__':
    unittest.main()
