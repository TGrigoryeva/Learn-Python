# Подключим необходимые компоненты
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey  # ForeignKey - отвечает за связь с другой таблицей
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///steam.sqlite')  # выбираем БД, с которой будем работать (в данном случае sqlite). файл с БД будет называться blog.sqlite

db_session = scoped_session(sessionmaker(bind=engine))  # соединение с БД (получение-отправка данных)

Base = declarative_base()  # связываем сессию с БД. Декларативная база, т.е. опишем структуру таблиц в питон коде
Base.query = db_session.query_property()  # привязываем к declarative_base возможность делать запросы к БД


# Добавим описание таблицы:
class User(Base):  # i.e. class users derives from class base all capabilities
    __tablename__ = 'users'  # name of DB - "users"
    id = Column(Integer, primary_key=True)  # creating of columns for DB table. primary_key=True - it mrans ID will be primary key
    username = Column(String(100), unique=True)# 100 length of string (customized value)
 
    def __init__(self, username=None):  # эти переменные будем присваивать атрибутам класса (выше)
        self.username = username # это обращения к своему собственному атрибуту

    def __repr__(self):  # то, что выведется на print
        return '<User {}>'.format(self.username)

class Games(Base): # создаем новый класс и таблицу
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer,unique=True)
    discount = Column(Float)

    def __init__(self, game_id=None, discount=None):
        self.game_id = game_id
        self.discount = discount

    def __repr__(self):
        return '<Games {} {} >'.format(self.game_id, self.discount)

class User_Game(Base): # создаем таблицу связей
    __tablename__ = 'user_game'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer,ForeignKey('games.id'))
    user_id = Column(Integer,ForeignKey('users.id'))

    def __init__(self, game_id=None, user_id=None):
        self.game_id = game_id
        self.user_id = user_id

    def __repr__(self):
        return '<User_Game {} {} >'.format(self.game_id,self.user_id)

# Создадим нашу базу данных:
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
