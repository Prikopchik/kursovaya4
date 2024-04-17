import requests

class APIClient:
    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies?text={search_query}"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            return response.json()['items']
        except requests.RequestException as e:
            print("Ошибка при получении данных:", e)
            return []