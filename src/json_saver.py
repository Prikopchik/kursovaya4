import json
from .data_saver_loader import DataSaverLoader


class JSONSaver(DataSaverLoader):
    def __init__(self, filename):
        self.filename = filename

    def save_vacancies_to_json(self, vacancies_data, file_path) -> None:
        try:
            with open(file_path, 'w', encoding="utf-8") as file:
                json.dump(vacancies_data, file, indent=4)
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)

    def load_vacancies_from_json(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print("Ошибка при чтении данных из файла:", e)
            return {}
