from .vacancy import Vacancy
from .vacancy_api import VacancyAPI
import requests
from urllib.parse import urljoin


class SuperJobApiClient(VacancyAPI):
    base_url = 'https://superjob.api'

    def get_vacancies(self, search_query):
        url = urljoin(self.base_url, 'vacancies')
        params = {'keyword': search_query}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            vacancies_data = response.json()['items']
            vacancies = [Vacancy(vacancy_data) for vacancy_data in vacancies_data]
            return vacancies
        except requests.RequestException as e:
            print("Ошибка при получении данных от SuperJob API:", e)
            return []
