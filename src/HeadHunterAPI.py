import requests
import src.VacancyAPI as VacancyAPI
import json

class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies?text={search_query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []

    def save_vacancies_to_json(vacancies_data, file_path):
        with open(file_path, 'w') as file:
            json.dump(vacancies_data, file, indent=4)