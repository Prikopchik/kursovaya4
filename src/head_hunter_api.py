import requests
import json
from vacancy_api import VacancyAPI

class HeadHunterAPI(VacancyAPI):
    def __init__(self, api_client, json_saver):
        self.api_client = api_client
        self.json_saver = json_saver

    def get_vacancies(self, search_query):
        vacancies_data = self.api_client.get_vacancies(search_query)
        self.json_saver.save_vacancies_to_json(vacancies_data, "data/vacancies.json")
        return vacancies_data

    def add_vacancy(self, vacancy_data, file_path):
        try:
            vacancies = self.load_vacancies_from_json(file_path)
            vacancies.append(vacancy_data)
            self.save_vacancies_to_json(vacancies, file_path)
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)

    def filter_vacancies(self, search_query, file_path):
        try:
            vacancies = self.load_vacancies_from_json(file_path)
            filtered_vacancies = [vacancy for vacancy in vacancies if search_query in vacancy['name']]
            return filtered_vacancies
        except IOError as e:
            print("Ошибка при чтении данных из файла:", e)
            return []

    def delete_vacancy(self, vacancy_id, file_path):
        try:
            vacancies = self.load_vacancies_from_json(file_path)
            vacancies = [vacancy for vacancy in vacancies if vacancy['id'] != vacancy_id]
            self.save_vacancies_to_json(vacancies, file_path)
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)

    def save_vacancies_to_json(self, vacancies_data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(vacancies_data, file, indent=4)
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)
