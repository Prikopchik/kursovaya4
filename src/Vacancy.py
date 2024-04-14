import json

class Vacancy:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.employer = data['employer']['name']
        
        salary_data = data.get('salary')
        if salary_data:
            self.salary_from = salary_data.get('from')
            self.salary_to = salary_data.get('to')
            self.currency = salary_data.get('currency')
        else:
            self.salary_from = None
            self.salary_to = None
            self.currency = None
        
        self.area = data['area']['name']
        self.requirement = data['snippet']['requirement']
        self.responsibility = data['snippet']['responsibility']
        self.published_at = data['published_at']

    def __repr__(self):
        return f"Vacancy(title='{self.title}', salary='{self.salary}')"
