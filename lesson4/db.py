# Подключим необходимые компоненты
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey  # ForeignKey - отвечает за связь с другой таблицей
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///blog.sqlite')  # выбираем БД, с которой будем работать (в данном случае sqlite). файл с БД будет называться blog.sqlite

db_session = scoped_session(sessionmaker(bind=engine))  # соединение с БД (получение-отправка данных)

Base = declarative_base()  # связываем сессию с БД. Декларативная база, т.е. опишем структуру таблиц в питон коде
Base.query = db_session.query_property()  # привязываем к declarative_base возможность делать запросы к БД


# Добавим описание таблицы:
class User(Base):  # i.e. class users derives from class base all capabilities
    __tablename__ = 'users'  # name of DB - "users"
    id = Column(Integer, primary_key=True)  # creating of columns for DB table. primary_key=True - it mrans ID will be primary key
    first_name = Column(String(50))  # 50 - length of string (customized value)
    last_name = Column(String(50))
    email = Column(String(120), unique=True)  # unique=True - means DB can check uniqueness of e-mail
    posts = relationship('Post', backref='author') # добавили описание связи в User, relationship - связи между таблицамию backref - то, как связт выглядит со стороны класса post
    
    def __init__(self, first_name=None, last_name=None, email=None):  # эти переменные будем присваивать атрибутам класса (выше)
        self.first_name = first_name # это обращения к своему собственному атрибуту
        self.last_name = last_name
        self.email = email

    def __repr__(self):  # 
        return '<User {} {} {}>'.format(self.first_name, self.last_name,self.email)

class Post(Base): # создаем новый класс и таблицу
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id')) # в таблице User называется просто ID. связка делается по id

    def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
        self.title = title
        self.image = image
        self.published = published
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post {}>'.format(self.title)



# Создадим нашу базу данных:
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

'''
SQLite встроен в питон и при использовании файл БД создастся автоматически
__init__ - class constructor. 

Добавим в таблицу данные:
>>> from db import db_session, User
>>> me = User('Михаил', 'Корнеев', 'mike@python.ru') # в переменную кладем объект класса
>>> me.email
'mike@python.ru'

Добавим в БД данные:
>>> db_session.add(me) 
>>> db_session.commit()

Поменяем e-mail пользователя:
>>> me.email='korneevm@gmail.com'
>>> db_session.commit()

Выборка данных
>>> from db import User
>>> u = User
>>> u
<class 'db.User'>
>>> u.query.all()

Фильтры

>>> u.query.filter(User.first_name=='Маша').first() # first() - получить первое совпадение
<User Маша Иванова mari@example.com>

>>> u.query.filter(User.first_name.like('М%')).all()
[<User Михаил Корнеев korneevm@gmail.com>, 
    <User Маша Иванова mari@example.com>]

Сортировка

По возрастанию (от а до я)
u = User
>>> u.query.order_by(User.email).all()
По убыванию (от я до а)
>>> u.query.order_by(User.email.desc()).all()  # desc - убывание
Объединение методов
>>> u.query.filter(User.last_name.like('%ов%'))
        .order_by(User.first_name).all() # отсортированные по имени по возрастанию

Связи между таблицами
Проимпортируем еще несколько типов данных

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
И создадим таблицу posts
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
И создадим таблицу posts
class Post(Base):
    ...

    def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
        self.title = title
        self.image = image
        self.published = published
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post {}>'.format(self.title)

Добавим описание связи в User

Это делается при помощи orm.relationship
from sqlalchemy.orm import relationship
В описании класса она используется так:
posts = relationship('Post', backref='author')
Получим данные автора поста
>>> from db import Post
>>> p = Post
>>> blog_post = p.query.get(1) # 1 - идентификатор поста
>>> blog_post.author
<User Василий Петров vasya@example.com>
>>> blog_post.author.email
'vasya@example.com'
Получим список постов автора
>>> vasya = blog_post.author
>>> vasya
<User Василий Петров vasya@example.com>
>>> vasya.posts


'''