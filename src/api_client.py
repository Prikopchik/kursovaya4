from urllib.parse import urljoin

import requests


class APIClient:
    base_url = 'https://api.hh.ru'

    def get_vacancies(self, search_query):
        url = urljoin(self.base_url, 'vacancies')
        params = {'text': search_query}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()['items']
        except requests.RequestException as e:
            print("Ошибка при получении данных:", e)
            return []