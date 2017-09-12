import csv

# словарь с ответами
answers = {
"привет":"И тебе привет!",
"как дела":"Лучше всех",
"пока":"Увидимся" }

# метод 1
with open("output.csv", 'w', encoding = "utf-16") as f:
    for key, value in answers.items():
        f.write( '%s;%s\n' % (key, value) )

# метод 2 с использованием модуля CSV
with open("output.csv", "w", encoding = "utf-16") as f:
    csv_writer = csv.writer(f, delimiter=';', lineterminator = '\n')
    csv_writer.writerows(answers.items()) # в writerows уже встроены циклы в отличие от writerow


'''
with open ("export_get_answer.csv", "w", encoding = "utf-8") as f:
    fields = ["привет","как дела","пока"] 
    writer = csv.DictWriter(f, fields , delimiter = ";")
 #   writer.writeheader() #Write a row with the field names 
    for key in answers:  #проходит по каждой паре ключ-значение и записывает в отдельной строке
        
        writer.writerow(key) 
        print(key)
f.close()
'''
