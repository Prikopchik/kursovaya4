from src.vacancy import Vacancy
from src.vacancy_api import VacancyAPI
import requests
from urllib.parse import urljoin


class HHApiClient(VacancyAPI):
    base_url = 'https://api.hh.ru'

    def get_vacancies(self, search_query: str) -> Vacancy:
        url = urljoin(self.base_url, 'vacancies')
        params = {'text': search_query}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            vacancies_data = response.json()['items']
            vacancies = [Vacancy(data) for data in vacancies_data]
            return vacancies
        except requests.RequestException as e:
            print("Ошибка при получении данных:", e)
            return []
