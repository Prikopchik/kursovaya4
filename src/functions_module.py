def filter_vacancies(vacancies, keywords):
    if not keywords:  
        return vacancies

    return [vacancy for vacancy in vacancies if any(keyword.lower() in (vacancy.name or '').lower() or 
                                                    keyword.lower() in (vacancy.requirement or '').lower() 
                                                    for keyword in keywords)]


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
