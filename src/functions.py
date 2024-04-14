def filter_vacancies(vacancies, keywords):
    filtered_vacancies = []
    for vacancy in vacancies:
        for keyword in keywords:
            if keyword.lower() in vacancy.description.lower():
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies

def get_vacancies_by_salary(vacancies, salary_range):
    ranged_vacancies = []
    min_salary, max_salary = map(int, salary_range.split('-'))
    for vacancy in vacancies:
        salary = vacancy.salary
        if salary.isdigit():
            if min_salary <= int(salary) <= max_salary:
                ranged_vacancies.append(vacancy)
        else:
            pass
    return ranged_vacancies

def sort_vacancies(vacancies):
    sorted_vacancies = sorted(vacancies, key=lambda x: int(x.salary), reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies, n):
    return vacancies[:n]

def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy.title, vacancy.salary)