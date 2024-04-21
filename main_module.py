from src.head_hunter_api import HHApiClient
from src.vacancy import Vacancy  
from src.api_client import APIClient
from src.functions_module import sort_vacancies, get_top_vacancies, get_vacancies_by_salary, filter_vacancies, print_vacancies
from src.json_saver import JSONSaver
from src.superjob_api_client import SuperJobApiClient

def main():
    try:
        hh_api_client = HHApiClient()
        sj_api_client = SuperJobApiClient()

        search_query = input("Введите поисковый запрос: ")
        hh_vacancies = hh_api_client.get_vacancies(search_query)
        #sj_vacancies = sj_api_client.get_vacancies(search_query)

        vacancies_list = [
            Vacancy(vacancy) for vacancy in hh_vacancies] #+sj_vacancies
        

        top_n = int(input("Введите количество вакансий для вывода: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        salary_range = input("Введите диапазон зарплат: ")

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    except Exception as e:
        print("Произошла ошибка:", e)
if __name__ == "__main__":
    main()
