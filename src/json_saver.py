import json

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def save_vacancies_to_json(self, vacancies_data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(vacancies_data, file, indent=4)
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)

    def load_vacancies_from_json(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print("Ошибка при чтении данных из файла:", e)
            return {}
