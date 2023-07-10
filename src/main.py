from HeadHunter_API import HeadHunterAPI

def main():
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

    for value in data_values:
        company = HeadHunterAPI(value)
        company.get_vacancies()
        company.get_company_info()
        company.formate_vacancies()
        company.write_information_to_the_database()

if __name__ == "__main__":
    main()
