# CourseWork_5

Данная программа считывает вакансии нужных компаний по id компаний и сохраняет результат в базе данных postgres.
Также создан класс по работе с базой данных, в котором реализовано несколько методов.

Для того, чтобы программа заработала нужно создать таблицы в pgadmin, код для их создания представлен в queries.sql

![image](https://github.com/Vosida87/CourseWork_5/assets/129009216/e0562d03-879e-4ff3-9fcb-8335a87d2d7b)


Далее нужно предоставить свои данные для соединения с БД, нужно ввести их в методе write_information_to_the_database() в классе HeadHunterAPI

![image](https://github.com/Vosida87/CourseWork_5/assets/129009216/36fce3ff-d634-426a-996c-486b7e0df9b8)


Также нужно ввести данные в методе make_connection() класса DBManager

![image](https://github.com/Vosida87/CourseWork_5/assets/129009216/e1bcffce-693d-4c25-832e-a0d70eef9e18)


Они могут быть такими:

(host='localhost',
database='CourseWork_5',
user='postgres',
password='(ну и ваш пароль)')


Ну и в файле main при запуске код программы полностью реализуется.
