import head_hunter_api as head_hunter_api
from src.vacancy import Vacancy  
from functions_module import sort_vacancies, get_top_vacancies, get_vacancies_by_salary, filter_vacancies, print_vacancies

def main():
    try:
        hh_api = head_hunter_api.HeadHunterAPI()

        search_query = input("Введите поисковый запрос: ")
        hh_vacancies = hh_api.get_vacancies(search_query)
        vacancies_list = [Vacancy(vacancy) for vacancy in hh_vacancies]  

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
