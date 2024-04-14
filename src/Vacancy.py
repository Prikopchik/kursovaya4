import json

class Vacancy:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.employer = data['employer']['name']
        self.salary_from = data['salary']['from']
        self.salary_to = data['salary']['to']
        self.currency = data['salary']['currency']
        self.area = data['area']['name']
        self.requirement = data['snippet']['requirement']
        self.responsibility = data['snippet']['responsibility']
        self.published_at = data['published_at']

    def __repr__(self):
        return f"Vacancy(title='{self.title}', salary='{self.salary}')"

    def load_vacancies_from_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Vacancy(item) for item in data['items']]

    file_path = 'data/vacancies.json'
    vacancies_list = load_vacancies_from_json(file_path)

    def compare_salary(self, other):
        if not self.salary.isdigit() or not other.salary.isdigit():
            return 0
        return int(self.salary) - int(other.salary)
