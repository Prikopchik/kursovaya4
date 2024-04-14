import src.JSONSaver as JSONSaver, src.Vacancy as Vacancy, src.VacancyAPI as VacancyAPI, src.HeadHunterAPI as HeadHunterAPI
from src.functions import sort_vacancies,get_top_vacancies,get_vacancies_by_salary,filter_vacancies,print_vacancies
def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy(**vacancy) for vacancy in hh_vacancies]

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()
