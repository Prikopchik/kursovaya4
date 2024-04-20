from abc import ABC, abstractmethod
from vacancy import Vacancy

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> Vacancy:
        pass
