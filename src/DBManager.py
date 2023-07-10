import psycopg2


class DBManager:
    @classmethod
    def make_connection(cls):
        """
        соединяет класс с базой данных
        !!!!(НУЖНО ВПИСАТЬ СВОИ ДАННЫЕ ДЛЯ СОЕДИНЕНИЯ)!!!!
        """
        connection = psycopg2.connect(
            host='',
            database='',
            user='',
            password='',
        )
        return connection

    @staticmethod
    def get_companies_and_vacancies_count():
        """
        получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = DBManager.make_connection()
        with conn.cursor() as cur:
            cur.execute(f"SELECT company_name, count_of_vacancies FROM companies")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()

    @staticmethod
    def get_all_vacancies():
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = DBManager.make_connection()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT vacancies.vacancy_name, vacancies.salary_from, "
                f"vacancies.salary_to, vacancies.vacancy_url, companies.company_name\n"
                f"FROM vacancies\n"
                f"JOIN companies USING(company_id)"
                        )
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()

    @staticmethod
    def get_avg_salary():
        """
        получает среднюю зарплату по вакансиям.
        """
        conn = DBManager.make_connection()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT AVG (salary_to)\n"
                f"FROM vacancies"
                        )
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary():
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        conn = DBManager.make_connection()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT vacancies.vacancy_name, vacancies.salary_from, \n"
                f"vacancies.salary_to, vacancies.vacancy_url\n"
                f"FROM vacancies\n"
                f"WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)\n"
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()

    @staticmethod
    def get_vacancies_with_keyword(keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        """
        conn = DBManager.make_connection()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT * FROM vacancies\n"
                f"WHERE vacancy_name LIKE '%{keyword}%'"
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()
