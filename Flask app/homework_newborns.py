'''
Получение данных

На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных. 
Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json. 
Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows

'''
import requests # позволяет получать инфо от сервера


def get_newborns_names(url):
    result = requests.get(url)
 #   print(result.json()) # FYI метод со скобками, аттрибут - внутри. Мы получим не строку, а DICT
    if result.status_code == 200: #нужно всегда проверять, что вернул сервер
        return result.json()
    else:
        print("Something went wrong")
    

if __name__ == "__main__":
    data = get_newborns_names("https://apidata.mos.ru/v1/datasets/2009/rows/?api_key=c6a37e0e2a6057df193aee1ade88e16f")
    print(data)


'''
при вызове функции мы получили данные в формате json. это НЕ питоновский словарь, но питон может ее преобразовать
у request есть функция для такого преобразования json

("https://apidata.mos.ru/v1/datasets/2009/rows/?api_key=c6a37e0e2a6057df193aee1ade88e16f")
'''

