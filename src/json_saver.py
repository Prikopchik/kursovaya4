import json
import os

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        try:
            with open(self.filename, 'a') as file:
                json.dump(vacancy.__dict__, file)
                file.write('\n')
        except IOError as e:
            print("Ошибка при записи данных в файл:", e)

    def update_vacancy(self, vacancy_id, updated_data):
        try:
            with open(self.filename, 'r+') as file:
                data = json.load(file)
                for item in data['items']:
                    if item['id'] == vacancy_id:
                        item.update(updated_data)
                        break
                file.seek(0)
                json.dump(data, file, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            print("Ошибка при обновлении данных в файле:", e)

    def delete_vacancy(self, vacancy):
        try:
            temp_file = self.filename + '.tmp'
            with open(self.filename, 'r') as file, open(temp_file, 'w') as temp:
                for line in file:
                    data = json.loads(line)
                    if data.get('title') != vacancy.title:
                        temp.write(line)
            os.remove(self.filename)
            os.rename(temp_file, self.filename)
        except (IOError, json.JSONDecodeError) as e:
            print("Ошибка при удалении данных из файла:", e)

    def clear_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump({"items": []}, file, indent=4)
        except IOError as e:
            print("Ошибка при очистке файла:", e)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print("Ошибка при чтении данных из файла:", e)
            return {}
