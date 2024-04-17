from .vacancy import Vacancy

class HeadHunterAPI:
    def __init__(self, api_client, json_saver):
        self.api_client = api_client
        self.json_saver = json_saver

    def get_vacancies(self, search_query):
        vacancies_data = self.api_client.get_vacancies(search_query)
        self.json_saver.save_vacancies_to_json(vacancies_data, "data/vacancies.json")
        return vacancies_data

    def filter_vacancies(self, search_query, file_path):
        vacancies = self.json_saver.load_vacancies_from_json(file_path)
        filtered_vacancies = [vacancy for vacancy in vacancies if search_query in vacancy['name']]
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id, file_path):
        vacancies = self.json_saver.load_vacancies_from_json(file_path)
        vacancies = [vacancy for vacancy in vacancies if vacancy['id'] != vacancy_id]
        self.json_saver.save_vacancies_to_json(vacancies, file_path)
