import unittest
from vacancy import Vacancy
from functions_module import filter_vacancies, sort_vacancies, get_top_vacancies

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
