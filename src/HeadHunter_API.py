import requests
import json


class HeadHunterAPI:
    """
    Класс для получения вакансий из HeadHunter по api
    инициализируется по id компании
    """
    def __init__(self, company_id):
        self.company_id = company_id
        self.vacancies_url = "https://api.hh.ru/vacancies"
        self.company_url = f"https://api.hh.ru/employers/{self.company_id}"
        # "self.vacancies_url":"https://api.hh.ru/vacancies?employer_id=self.employer_id"
        self.params = {"per_page": 50,
                       "employer_id": self.company_id,
                       }
        self.headers = {"User-Agent": "MyApp 1.0"}
        self.vacancies = []
        self.company_info = []

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.company_id}', {int(self.vacancies_url)}, {self.params})"

    def get_vacancies(self):
        """
        функция запроса, возвращает вакансии компании
        """
        response = requests.get(self.vacancies_url, params=self.params, headers=self.headers)
        json_response = response.json()['items']
        for vacancy in json_response:
            self.vacancies.append(vacancy)
        return json_response

    def get_company_info(self):
        """
        функция запроса, возращает информацию о компании
        """
        response = requests.get(self.company_url)
        company_data = response.json()
        self.company_info.append(company_data)
        return company_data
