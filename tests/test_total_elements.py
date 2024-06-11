import requests
import unittest
from .config import BASE_URL

class TestTotalElements(unittest.TestCase):

    def test_total_elements(self):
        # Проверка total на соответствие фактическому кол-ву регионов
        response = requests.get(f"{BASE_URL}?page_size=5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        total_items = data['total']
        page_size = 5
        total_count = 0
        page = 1

        while True:
            response = requests.get(f"{BASE_URL}?page_size={page_size}&page={page}")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            items = data.get('items', [])
            total_count += len(items)
            if len(items) < page_size:
                break
            page += 1

        self.assertEqual(total_items, total_count,f"Фактическое количество элементов ({total_count}) не соответствует total ({total_items})")

    def test_total_parameter_with_query(self):
        # Тест проверки параметра 'total' на соответствие общему кол-ву элементов по запросу с параметром 'q'
        query = "нов"
        response = requests.get(f"{BASE_URL}?q={query}&page_size=5&page=1")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        total_items = data['total']
        total_count = 0
        page = 1

        while True:
            response = requests.get(f"{BASE_URL}?q={query}&page_size=5&page={page}")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            total_count += len(data['items'])
            if len(data['items']) < 5:
                break
            page += 1

        self.assertEqual(total_items, total_count,"Параметр 'total' не соответствует фактическому количеству элементов")

    def test_no_duplicate_elements_across_pages(self):
        # Проверка, что элементы не дублируются на следующих страницах
        page_size = 5
        seen_ids = set()
        page = 1

        while True:
            response = requests.get(f"{BASE_URL}?page_size={page_size}&page={page}")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            items = data.get('items', [])
            for item in items:
                self.assertNotIn(item['id'], seen_ids, f"Элемент с ID {item['id']} дублируется на странице {page}")
                seen_ids.add(item['id'])
            if len(items) < page_size:
                break
            page += 1

if __name__ == '__main__':
    unittest.main()