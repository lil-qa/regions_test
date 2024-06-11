import requests
import unittest
from .config import BASE_URL

class TestPageSize(unittest.TestCase):

    def test_page_size_5(self):
        # Тест проверки размера страницы (не более 5 элементов)
        response = requests.get(f"{BASE_URL}?page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        self.assertLessEqual(len(data['items']), 5, "Количество элементов на странице превышает 5")

    def test_page_size_10(self):
        # Тест проверки размера страницы (не более 10 элементов)
        response = requests.get(f"{BASE_URL}?page_size=10")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        self.assertLessEqual(len(data['items']), 10, "Количество элементов на странице превышает 10")

    def test_page_size_15(self):
        # Тест проверки размера страницы (не более 15 элементов)
        response = requests.get(f"{BASE_URL}?page_size=15")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data, "Параметр 'items' отсутствует в ответе")
        self.assertIsInstance(data['items'], list, "Параметр 'items' должен быть списком")
        self.assertLessEqual(len(data['items']), 15, "Количество элементов на странице превышает 15")

    def test_page_size_0_error(self):
        # Тест проверки ошибки при вводе значения "0" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=0")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_4_error(self):
        # Тест проверки ошибки при вводе значения "4" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=4")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_6_error(self):
        # Тест проверки ошибки при вводе значения "6" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=6")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_9_error(self):
        # Тест проверки ошибки при вводе значения "9" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=9")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_11_error(self):
        # Тест проверки ошибки при вводе значения "11" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=11")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_14_error(self):
        # Тест проверки ошибки при вводе значения "14" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=14")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_page_size_16_error(self):
        # Тест проверки ошибки при вводе значения "16" в параметр page_size
        response = requests.get(f"{BASE_URL}?page_size=16")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data, "Параметр 'error' отсутствует в ответе")
        self.assertIn('message', data['error'], "Параметр 'message' отсутствует в ответе об ошибке")
        self.assertEqual(data['error']['message'], "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", "Некорректное сообщение об ошибке для параметра 'page_size'")

    def test_default_page_size(self):
        # Тест проверки значения page_size по умолчанию (не более 15 элементов)
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data)
        self.assertIsInstance(data['items'], list)
        self.assertEqual(len(data['items']), 15, "Количество элементов на странице по умолчанию должно быть 15")

if __name__ == '__main__':
    unittest.main()
