def filter_vacancies(vacancies, keywords):
    if not keywords:  
        return vacancies

    filtered_vacancies = []
    for vacancy in vacancies:
        for keyword in keywords:
            if keyword.lower() in vacancy.name.lower() or keyword.lower() in vacancy.requirement.lower():
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def get_vacancies_by_salary(vacancies, salary_range):
    ranged_vacancies = []
    min_salary, max_salary = map(int, salary_range.split('-'))
    for vacancy in vacancies:
        if vacancy.salary_from is not None and vacancy.salary_to is not None:
            if min_salary <= vacancy.salary_to <= max_salary or min_salary <= vacancy.salary_from <= max_salary:
                ranged_vacancies.append(vacancy)
        elif vacancy.salary_from is not None:
            if min_salary <= vacancy.salary_from <= max_salary:
                ranged_vacancies.append(vacancy)
        elif vacancy.salary_to is not None:
            if min_salary <= vacancy.salary_to <= max_salary:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies):
    sorted_vacancies = sorted(vacancies, key=lambda x: int(x.salary_to if x.salary_to is not None else 0), reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies, n):
    return vacancies[:n]

def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy.name, vacancy.salary_to)
