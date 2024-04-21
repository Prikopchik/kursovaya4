class Vacancy:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.employer = data.get('employer', {}).get('name')
        
        salary_data = data.get('salary')
        if salary_data:
            self.salary_from = salary_data.get('from')
            self.salary_to = salary_data.get('to')
            self.currency = salary_data.get('currency')
        else:
            self.salary_from = None
            self.salary_to = None
            self.currency = None
        
        self.area = data.get('area', {}).get('name')
        self.requirement = data.get('snippet', {}).get('requirement')
        self.responsibility = data.get('snippet', {}).get('responsibility')
        self.published_at = data.get('published_at')

    def __repr__(self):
        return f"Vacancy(title='{self.name}', salary_from='{self.salary_from}', salary_to='{self.salary_to}', currency='{self.currency}')"

