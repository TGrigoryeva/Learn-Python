from steambot import get_info  # нужна ли эта функция?
import requests
import json
from bs4 import BeautifulSoup
import re
from steam_db import db_session, Games, User, User_Game
from sqlalchemy import exc
from sqlalchemy.orm import relationship

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException:
        print ("Error")
        return False

username = "naash71"  # будет вводиться пользователем в сообщении telegram
html = get_html("https://steamcommunity.com/id/%s/wishlist/" % (username))
#print(html)

db_user = User.query.filter(User.username == username).first()  # будет значение None, если таких данных нет
# add new username to DB 
if db_user is None:
    db_session.add(User(username))
    db_user = User.query.filter(User.username == username).first()  # <User naash71> - то, что получим

user_db_id = db_user.id  # get database user id

# get list of user games from DB
g = db_session.query(Games).filter(Games.user.any(User.username == username)).all()  # get db_usergames through filter by username
db_usergames = []
for row in g:
    db_usergames.append(row.game_id)

bs = BeautifulSoup(html, "html.parser")
wish_games = bs.find_all("div", "wishlistRow")
all_games = []

# нашли ID игр из WISHLIST пользователя

for game in wish_games:
    game_id = re.search(r'([0-9]+)', game['id']).group(0)
    all_games.append(int(game_id))
# нашли цены по ID игры из WISHLIST

    data = get_info("http://store.steampowered.com/api/appdetails?appids=%s&cc=ru" % (game_id))
    game_name = data[game_id]["data"]["name"]
    try:  # в Steam бывают игры без цены. устраняем KeyError. В БД не попадет
        prices = data[game_id]["data"]["price_overview"]
    except KeyError:
        print(game_name)
        print("Цена для данного продукта отсутствует\n")       
        continue
    print(game_name)
    print("http://store.steampowered.com/app/%s" % (game_id))

    if prices["discount_percent"] == 0:
        print(prices["initial"]/100,"RUB")
    else:
        print(prices["final"]/100,"RUB,","Скидка:",prices["discount_percent"],"%\nСтарая цена:", prices["initial"]/100,"RUB") 
    print("\n")

    db_game = Games.query.filter(Games.game_id == game_id).first()
    if db_game is None:
        db_session.add(Games(game_id, prices["discount_percent"]))  # new game added to database
        db_game = Games.query.filter(Games.game_id == game_id).first()
    else:
        db_game.discount = prices["discount_percent"]  # update discounts
        
    game_db_id = db_game.id # get database game id
    # new unique relationship user-game added. If entry already exist, raise exception:
    try:
        db_session.add(User_Game(game_db_id, user_db_id))
        db_session.flush()
    except exc.IntegrityError:
        db_session.rollback()

#  check if user has deleted game from steam wishlist
for value in db_usergames:
    if not db_usergames:
        print("db_usergames list is empty, pass")
    elif value not in all_games:
# if game has been removed from wishlist, remove entry from db User_Game table:        
        row_to_delete = db_session.query(User_Game).filter(User_Game.game_id == game_db_id, User_Game.user_id == user_db_id).all()
        print(row_to_delete,"row to delete")
        db_session.delete(row_to_delete)
        print("game {} deleted".format(value))

print(db_usergames,"db games")
print(all_games,"all games")

db_session.commit()

'''
PRICE HTML PARSER:
wish_games_price = bs.find_all("div", "gameListPriceData")
for price in wish_games_price:
    href = price.find("a")
    print(price.text, href.get("href"))
    
cron - планировщик задач (стартует скрипт по расписанию), либо запускаю скрипт в вечном цикле с функцией засыпания на 24 часа sys sleep
'''