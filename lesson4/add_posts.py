import csv
import datetime

from db import db_session, Post, User

posts_list = []
u = User

with open("blog.csv","r",encoding="utf-8") as f:
    fields = ["title","image","published","content","email","first_name","last_name"]
    reader = csv.DictReader(f, fields, delimiter=";")
    for row in reader:
        row["published"] = datetime.datetime.strptime(row["published"], "%d.%m.%y %H:%M")  # получаем дату из строки
        author = u.query.filter(User.email == row["email"]).first()
        row["user_id"] = author.id  # создали новую пару с ид пользователя

        posts_list.append(row)

# кладем полученные значения в БД

for post_data in posts_list:
    post = Post(post_data["title"], post_data["image"], post_data["published"], post_data["content"], post_data["user_id"]) # см def init
    db_session.add(post)

db_session.commit()