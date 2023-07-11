CREATE TABLE companies(
	company_id SERIAL PRIMARY KEY NOT NULL,
	company_name VARCHAR(100),
	company_url VARCHAR (100),
	company_info TEXT,
	count_of_vacancies INT
);

CREATE TABLE vacancies(
	company_id SERIAL REFERENCES companies(company_id) NOT NULL,
	vacancy_id INT UNIQUE,
	vacancy_name VARCHAR(100),
	vacancy_info TEXT,
	salary_from INT,
	salary_to INT,
	vacancy_url VARCHAR(100)
)