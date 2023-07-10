import requests
import psycopg2


class HeadHunterAPI:
    """
    Класс для получения вакансий из HeadHunter по api
    инициализируется по id компании
    """
    def __init__(self, company_id):
        self.company_id = company_id
        self.vacancies_url = "https://api.hh.ru/vacancies"
        self.company_url = f"https://api.hh.ru/employers/{self.company_id}"
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

    def formate_vacancies(self):
        """
        функция переформатирует список вакансий для запизи в базу данных
        """
        formatted_vacancies = []
        for vacancy in self.vacancies:
            if vacancy['salary'] is None:
                salary_from = None
                salary_to = None
            else:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
            formatted_vacancy = (self.company_id,
                                 vacancy['id'],
                                 vacancy['name'],
                                 vacancy['snippet']['responsibility'],
                                 salary_from,
                                 salary_to,
                                 vacancy['alternate_url']
                                 )
            formatted_vacancies.append(formatted_vacancy)
        self.vacancies = formatted_vacancies
        return self.vacancies

    def write_information_to_the_database(self):
        """
        функция запишет полученные данные в базу данных
        !!!!(НУЖНО ВПИСАТЬ СВОИ ДАННЫЕ ДЛЯ СОЕДИНЕНИЯ)!!!!
        """
        with psycopg2.connect(
                host='',
                database='',
                user='',
                password='',
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO companies VALUES (%s, %s, %s, %s, %s)", (
                    self.company_id,
                    self.company_info[0]['name'],
                    self.company_info[0]['alternate_url'],
                    self.company_info[0]['description'],
                    self.company_info[0]['open_vacancies'],
                )
                                )
                cur.executemany("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)", self.vacancies)

        conn.close()
