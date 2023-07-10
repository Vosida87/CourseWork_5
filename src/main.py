from HeadHunter_API import HeadHunterAPI
from DBManager import DBManager

# Импортируем классы для реализации программы


def main():

    # Создаём словарь с id компаниями, чтобы осуществить перебор

    company_id_dict = {'Пив&Ко': 865513,
                       'Мегафон': 3127,
                       'Easy Mebel': 5316954,
                       'ООО ИнтэлТорг': 5805779,
                       'ООО АктивПромКапитал': 9468763,
                       'Banks Soft Systems': 2575,
                       'Fir Service': 1479944,
                       'ООО Адванс Инжиниринг': 2135073,
                       'ALOEsmart': 3274487,
                       'ООО ИНТЕЛАЙТ': 3692182,
                       }

    data_values = company_id_dict.values()

    # Далее осуществляем перебор с методами класса HH,
    # А именно сохраняем данные с сайта по нужным компанями и загружаем в базу данных

    for value in data_values:
        company = HeadHunterAPI(value)
        company.get_vacancies()
        company.get_company_info()
        company.formate_vacancies()
        company.write_information_to_the_database()

    # Далее обращаемся  к менеджеру по работе с базой данных
    # Подробнее, что делают методы можно посмотреть в файле DBManager.py

    print('*' * 100)
    print(DBManager.get_companies_and_vacancies_count())
    print('*' * 100)
    print(DBManager.get_all_vacancies())
    print('*' * 100)
    print(DBManager.get_avg_salary())
    print('*' * 100)
    print(DBManager.get_vacancies_with_higher_salary())
    print('*' * 100)
    print(DBManager.get_vacancies_with_keyword('Python'))
    print('*' * 100)


if __name__ == "__main__":
    main()
