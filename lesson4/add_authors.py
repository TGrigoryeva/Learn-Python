from db import db_session, User

authors = [
{"first_name": "Василий",
"last_name": "Петров",
"email": "vasya@example.com"
},
{"first_name": "Маша",
"last_name": "Иванова",
"email": "mari@example.com"
},
{"first_name": "Полуэкт",
"last_name": "Невтруев",
"email": "p@example.com"
}
]

for a in authors:
    author = User(a["first_name"], a["last_name"], a["email"])  # создаем новый объект класса User и передаем туда словарь
    db_session.add(author)  # на каждом проходу цикла в БД добавляем новое инфо

db_session.commit()