import json
import os

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a') as file:
            json.dump(vacancy.__dict__, file)
            file.write('\n')

    def update_vacancy(self, vacancy_id, updated_data):
        with open(self.file_path, 'r+') as file:
            data = json.load(file)
            for item in data['items']:
                if item['id'] == vacancy_id:
                    item.update(updated_data)
                    break
            file.seek(0)
            json.dump(data, file, indent=4)

    def delete_vacancy(self, vacancy):
        temp_file = self.filename + '.tmp'
        with open(self.filename, 'r') as file, open(temp_file, 'w') as temp:
            for line in file:
                data = json.loads(line)
                if data.get('title') != vacancy.title:
                    temp.write(line)
        os.remove(self.filename)
        os.rename(temp_file, self.filename)

    def clear_file(self):
        with open(self.file_path, 'w') as file:
            json.dump({"items": []}, file, indent=4)

    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)
