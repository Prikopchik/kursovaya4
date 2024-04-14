import requests
import json
from src.VacancyAPI import VacancyAPI

class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies?text={search_query}"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            vacancies_data = response.json()['items']
            self.save_vacancies_to_json(vacancies_data, "data/vacancies.json")
            return vacancies_data
        except requests.RequestException as e:
            print("Ошибка при получении данных:", e)
            return []

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
