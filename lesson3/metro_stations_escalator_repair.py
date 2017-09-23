'''

Метро

В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.

Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539. 
'''
import json


with open("data-397-2017-09-06.json") as json_data:
    parsed_json = json.load(json_data) #тут получаем список со словарями

escalator_repair_list = []

for row in parsed_json:
    if len(row['RepairOfEscalators'])>0:
        if row['NameOfStation'] not in escalator_repair_list: #cтанции повторяются
            escalator_repair_list.append(row['NameOfStation'])

escalator_repair_list_string = "\n".join(sorted(escalator_repair_list)) # sorted - для вывода в алфавитном порядке

if len(escalator_repair_list)<1:
    print("Ни на одной станции не идет ремонт эскалаторов")
else:
    print("Ремонт эскалаторов идет на станциях:")
    print(escalator_repair_list_string)


