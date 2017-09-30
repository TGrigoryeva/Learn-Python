from steambot import get_info  # нужна ли эта функция?
import requests
import json
from bs4 import BeautifulSoup
import re
from steam_db import db_session, Games, User

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException:
        print ("Error")
        return False

username = "naash71"
html = get_html("https://steamcommunity.com/id/%s/wishlist/" % (username))
#print(html)

db_session.add(User(username))

bs = BeautifulSoup(html, "html.parser")
wish_games = bs.find_all("div", "wishlistRow")
wish_games_price = bs.find_all("div", "gameListPriceData")
all_games = []

# нашли ID игр из WISHLIST пользователя
for game in wish_games:
    game_id = re.search(r'([0-9]+)', game['id']).group(0)

# нашли цены по ID игры из WISHLIST

    data = get_info("http://store.steampowered.com/api/appdetails?appids=%s&cc=ru" % (game_id))
    name = data[game_id]["data"]["name"]
    try:
        prices = data[game_id]["data"]["price_overview"]
    except KeyError:
        print(name)
        print("Цена для данного продукта отсутствует\n")       
        continue
    print(name)
    print("http://store.steampowered.com/app/%s" % (game_id))

    if prices["discount_percent"] == 0:
        print(prices["initial"]/100,"RUB")
    else:
        print(prices["final"]/100,"RUB,","Скидка:",prices["discount_percent"],"%\nСтарая цена:", prices["initial"]/100,"RUB") 
    print("\n")

    db_session.add(Games(game_id, prices["discount_percent"], username.id))

db_session.commit()

'''
PRICE PARSER:

for price in wish_games_price:
    href = price.find("a")
    print(price.text, href.get("href"))

cron - планировщик задач (стартует скрипт по расписанию), либо запускаю скрипт в вечном цикле с функцией засывания на 24 часа sys sleep
'''