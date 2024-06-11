import requests
import unittest
from .config import BASE_URL

class TestCombined(unittest.TestCase):

    def test_combined_invalid_country_code_page_size_4(self):
        # Проверка недопустимых значений для код страны, номер страницы и кол-ва элементов на странице
        response = requests.get(f"{BASE_URL}?country_code=ру&page=к&page_size=4")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_invalid_page_and_page_size(self):
        # Проверка недопустимого значения для номер страницы и кол-ва элементов на странице
        response = requests.get(f"{BASE_URL}?country_code=ru&page=к&page_size=4")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_invalid_page_size(self):
        # Проверка недопустимого значения для кол-ва элементов на странице
        response = requests.get(f"{BASE_URL}?country_code=ru&page=1&page_size=4")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_valid_country_code_page_and_page_size(self):
        # Проверка корректных значений для кода страны, номер страницы и кол-ва элементов на странице
        response = requests.get(f"{BASE_URL}?country_code=ru&page=1&page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('items', data)
        self.assertIsInstance(data['items'], list)
        self.assertLessEqual(len(data['items']), 5)
        for item in data['items']:
            self.assertEqual(item['country']['code'], 'ru')

    def test_combined_invalid_country_code(self):
        # Проверка недопустимого значения для кода страны
        response = requests.get(f"{BASE_URL}?country_code=кк&page=1&page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_invalid_country_code_and_page(self):
        # Проверка недопустимых значений для кода страны и номер страницы
        response = requests.get(f"{BASE_URL}?country_code=кк&page=к&page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_invalid_country_code_and_page_size(self):
        # Проверка недопустимых значений для кода страны и кол-ва элементов на странице
        response = requests.get(f"{BASE_URL}?country_code=лл&page=1&page_size=4")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

    def test_combined_invalid_page(self):
        # Проверка недопустимого значения для номер страницы
        response = requests.get(f"{BASE_URL}?country_code=ru&page=к&page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data['error'])

if __name__ == '__main__':
    unittest.main()
