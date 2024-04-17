import unittest
from unittest.mock import MagicMock, patch
from head_hunter_api import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': [{'id': 1, 'name': 'Vacancy 1'}, {'id': 2, 'name': 'Vacancy 2'}]}
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies('Python')

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['name'], 'Vacancy 1')
        self.assertEqual(vacancies[1]['name'], 'Vacancy 2')

    @patch('src.HeadHunterAPI.requests.get')
    def test_get_vacancies_failure(self, mock_get):
        mock_get.return_value = MagicMock()
        mock_get.return_value.status_code = 500

        api = HeadHunterAPI.HeadHunterAPI()
        vacancies = api.get_vacancies('Python')

        self.assertEqual(vacancies, [])

if __name__ == '__main__':
    unittest.main()
