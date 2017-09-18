'''
Остановки

Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, 
вывести улицу, на которой больше всего остановок.

Названия строк  Количество по полю StationName
Варшавское шоссе    184
Калужское шоссе 143
проезд без названия 353
Общий итог  10748

'''

import csv


counter =0
street_dict = {} # создадим новый словарь улица - кол-во остановок

with open('data-398-2017-09-14.csv', 'r') as f:
    reader = csv.DictReader(f, fieldnames=None, delimiter=';')

    for row in reader:
        counter +=1 #тупо посчитали строки
        if row["Street"] in street_dict:
            street_dict[row["Street"]] += 1  
        else:
            street_dict[row["Street"]] = 1

    max_value = max(street_dict.values()) # нашли максимальное значение в словаре (кол-во остановок)

    for key, value in street_dict.items():  # находим ключ по максимальному значению (т.е. название остановки)
        if value == max_value:
            street = key


print("Максимальное количество остановок: ",max_value, "\nНа станции:", street)
print("Количество остановок: ", counter)



    #print(street_dict)

'''
Добавление нового элемента словаря:

    my_dict = {}

my_dict["abcd"] = 10

my_dict["qwer"] = 16

​

temp = "zxcvb"

my_dict[temp] = 33

​
OUT
my_dict

{'abcd': 10, 'qwer': 16, 'zxcvb': 33}
'''