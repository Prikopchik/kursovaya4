import unittest
from unittest.mock import MagicMock, patch
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.functions import filter_vacancies, sort_vacancies, get_top_vacancies

class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        # Мокируем успешный ответ от API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': [{'id': 1, 'name': 'Vacancy 1'}, {'id': 2, 'name': 'Vacancy 2'}]}
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies('Python')

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['name'], 'Vacancy 1')
        self.assertEqual(vacancies[1]['name'], 'Vacancy 2')

    @patch('requests.get')
    def test_get_vacancies_failure(self, mock_get):
        # Мокируем ответ с ошибкой от API
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies('Python')

        self.assertEqual(vacancies, [])

class TestFunctions(unittest.TestCase):
    def test_filter_vacancies(self):
        vacancies = [
            Vacancy({'id': 1, 'name': 'Python Developer', 'requirement': 'Python skills required'}),
            Vacancy({'id': 2, 'name': 'Java Developer', 'requirement': 'Java skills required'}),
            Vacancy({'id': 3, 'name': 'Frontend Developer', 'requirement': 'JavaScript skills required'}),
        ]
        filtered_vacancies = filter_vacancies(vacancies, ['Python'])
        self.assertEqual(len(filtered_vacancies), 1)
        self.assertEqual(filtered_vacancies[0].name, 'Python Developer')

    def test_sort_vacancies(self):
        vacancies = [
            Vacancy({'id': 1, 'name': 'Python Developer', 'salary_from': 80000}),
            Vacancy({'id': 2, 'name': 'Java Developer', 'salary_from': 90000}),
            Vacancy({'id': 3, 'name': 'Frontend Developer', 'salary_from': 70000}),
        ]
        sorted_vacancies = sort_vacancies(vacancies)
        self.assertEqual(sorted_vacancies[0].name, 'Java Developer')
        self.assertEqual(sorted_vacancies[1].name, 'Python Developer')
        self.assertEqual(sorted_vacancies[2].name, 'Frontend Developer')

    def test_get_top_vacancies(self):
        vacancies = [
            Vacancy({'id': 1, 'name': 'Python Developer', 'salary_from': 80000}),
            Vacancy({'id': 2, 'name': 'Java Developer', 'salary_from': 90000}),
            Vacancy({'id': 3, 'name': 'Frontend Developer', 'salary_from': 70000}),
        ]
        top_vacancies = get_top_vacancies(vacancies, 2)
        self.assertEqual(len(top_vacancies), 2)

if __name__ == '__main__':
    unittest.main()
