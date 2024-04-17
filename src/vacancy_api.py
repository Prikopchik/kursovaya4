from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy_data, file_path):
        pass

    @abstractmethod
    def filter_vacancies(self, search_query, file_path):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id, file_path):
        pass

    @abstractmethod
    def save_vacancies_to_json(self, vacancies_data, file_path):
        pass
