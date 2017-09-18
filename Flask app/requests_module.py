import requests # позволяет получать инфо от сервера


'''

result = requests.get("https://learn.python.ru")
result
result.status_code # например 200
result.headers # вернется словарь к которому можно обращаться 
result.encoding #  посмотреть кодировку
result.text # смотрим то, что вернул сервер
'''

'''

(env) c:\projects\lesson3>http "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=721cc70f0ae7cc5113819ebc393a8966"
'''

def get_weather(url):
    result = requests.get(url)
 #   print(result.json()) # FYI метод со скобками, аттрибут - внутри. Мы получим не строку, а DICT
    if result.status_code == 200: #нужно всегда проверять, что вернул сервер
        return result.json()
    else:
        print("Something went wrong")
    

if __name__ == "__main__":
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=721cc70f0ae7cc5113819ebc393a8966&units=metric") # или так по ID (последние цифры в браузере в адресной строке)
#    data = get_weather("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=721cc70f0ae7cc5113819ebc393a8966") #  APPID = (API KEY) 
    print(data)
    
'''
при вызове функции мы получили данные в формате json. это НЕ питоновский словарь, но питон может ее преобразовать
у request есть функция для такого преобразования json
'''
