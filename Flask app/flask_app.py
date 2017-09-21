'''

Задача

    Получим данные о температуре в Москве в Цельсиях
    Выведем на главной странице текущую дату, город и температуру


Вывод данных на сайте

Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных, получаемые при помощи функции из предыдущей задачи. Пример простейшего оформления таблицы - на следущейм слайде.

'''
from datetime import datetime
from news_list import all_news
from flask import Flask, abort, request  #  в return у FLASK всегда д.б. строка. abort, request - добавили для метода get, т.е. передача через url переменных
from requests_module import get_weather
from homework_newborns import get_newborns_names
import json

city_id = 524901 #ID города с сайта https://openweathermap.org/city/524901
apikey = "721cc70f0ae7cc5113819ebc393a8966" # API key с сайта openweathermap.org
apikey_mos_ru = "c6a37e0e2a6057df193aee1ade88e16f"
database_id = 2009

app = Flask(__name__) # создали переменную, содержащую приложение. name - название текущего файла
#@app.route("/") # привязываем к определенным адресам функции-обработчики. "/"  - означает главную страницу

@app.route("/") # создали страницу test. при помощи аппрута мы говорим какую страницу мы хотим формировать, т.е. по какому адрусу должен отвечать сервер. После нее идет функция, к-ая должна давать ответ на наш запрос
def index(): #функция, которая его обрабатывает
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)# % - для того, чтобы заменить в адресе буквы s на наши переменные/ для переменных добавляем ?
    weather = get_weather(url)

    current_date = datetime.now().strftime("%d.%m.%Y")
    print(current_date)

    result = "<p><b>Температура: %s</p><b>" % weather["main"]["temp"] # в ключе main есть словарь с ключом temp. Для обращения к элементам вложенного словаря соответственно необходимо использовать два ключа
    result += "<p><b>Город: %s</p><b>" % weather["name"]
    result += "<p><b>Дата: %s</p><b>" % current_date
    
    return result # 3 символа = длина контента (если смотреть в postman) также мы увидим тип text и кодировку utf-8 (все используют по умолчанию)
 # <news_id> - это шаблон. те в реальности мб что угодно.  в этой конструкции в адресе дб news и еще что-то/ При помощи INT мы говорим, что в этом месте в адресной строке дб целое число

@app.route("/news")
def all_the_news():
    colors = ["green","blue","maroon","magenta"]

#    var 1 for item in request.args: # item - переменные
#        print(item) # если в адресе будет http://127.0.0.1:5000/news?filter1=23, вернется news
#       print(request.args(item)) # амперсанд -разделитель переменных

#        return "News"

#   var 2 никогда так не делать:
#    limit = request.args.get("limit", "all") #положили переменную лимит либо то, что содержится в args по ключу лимит либо слово all. 
#    color = request.args.get("color", "black") # http://127.0.0.1:5000/news?filter1=23&color=green&limit=40
#    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit) # вернется all, если в url ввести фигню
    try:
        limit = int(request.args.get("limit")) #положили переменную лимит либо то, что содержится в args по ключу лимит либо слово all. 
    except:
        limit = 10 # значение по умолчанию, если ввод в url неверный
    color = request.args.get("color", "black") if request.args.get("color") in colors else  "black" # http://127.0.0.1:5000/news?filter1=23&color=green&limit=40
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit) # вернется all, если в url ввести фигню


@app.route("/news/<int:news_id>")
def news_by_id(news_id):

# ниже в переменную вернется список, если идентификатор найдется
# [news for news in all_news if news["id"] == news_id] - выбираем переменную news в цикле for news in all_news
# если news["id"] = то, что нам передали, происходит инициализация переменной news, а затем это попадет в переменную news to show

    news_to_show = [news for news in all_news if news["id"] == news_id] # в эту переменную могут списком вернуться словари, если идентификатор дублируется
    if len(news_to_show) == 1: # длина списка
        result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>)" # %(title)s - это именованный символ подстановки. так удобнее
        result = result % news_to_show[0] # через подстановку передаем словарь. news_to_show положили в отформатированный выше result!
        return result 
    else:
        abort(404)

@app.route("/names")
def newborns_names():

    years = ["2015","2016","2017"]
    url_mos_ru = "https://apidata.mos.ru/v1/datasets/%s/rows/?api_key=%s" % (database_id, apikey_mos_ru)
    n_names = get_newborns_names(url_mos_ru)

    year_filter = request.args.get("year") if request.args.get("year") in years else "all"

    header = '<html><head><title>newborns names</title></head><body background="https://im0-tub-ru.yandex.net/i?id=8b7cebe68bf3cd40861a6f9bb3d5d142-l&n=13"><b>Сведения о наиболее популярных женских именах среди новорожденных</b><br><a href="https://data.mos.ru/opendata/2009">с этого сайта</a><br><br> <table border="1"> <tr><th>Number</th><th>Year</th><th>Name</th></tr>'
    footer = '</table> </body></html>'

    list_of_names = [header]

    if year_filter == "all":
        for n in n_names:
            list_of_names.append('<tr><td>') # tr открытие строки, td - открытие ячейки
            list_of_names.append( '</td><td>'.join(map(str, [ n["Number"], n["Cells"]["Year"], n["Cells"]["Name"] ] )))
            list_of_names.append('</td></tr>')
    else:
        for n in n_names:
            if int(year_filter) == n["Cells"]["Year"]:
                list_of_names.append('<tr><td>') # tr открытие строки, td - открытие ячейки
                list_of_names.append( '</td><td>'.join(map(str, [ n["Number"], n["Cells"]["Year"], n["Cells"]["Name"] ] )))
                list_of_names.append('</td></tr>')            


    list_of_names.append(footer)

    string_of_names = ''.join(list_of_names) # преобразовали лист в string

    return string_of_names


# делаем так,чтобы flask приложение умело запускаться. 
if __name__ == "__main__": #если файл запускается напрямую, значит надо запускать приложение
    app.run(port = 5000, debug = True) # 127.0.0.1 - local host, т.е. внутренний адрес компа. К этому ажресу можно получить доступ только с самого  :5000 - это порт. 80 порт - стандартный для всех web-адресов. 



''' 
\n html игнорирует, поэтому переносим иначе строку)
<p> - новый абзац
<br> - разрыв строки
<b> - жирное выделение
<h1> - главный заголовок сраницы
<i> - наклонный текст
<tr> - открытие строки
<th> - открытие ячейки
% такая подстановка хороша тем, что у нас всегда будет на выходе строка, даже если ранее у переменной был тип int
сложные параметры (например, фильтры), неэффективно передавать через URL, поэтому используем GET
'''