mylist = [10,20,30,40,50,60,70,80,90,100] #task 1
for score in mylist:
    print(score+1)


user_input=input("Введите любу строку: ") #task 2
for character in user_input:
    print(character)


#task 3
list_of_pupils=[
{'school_class': "4a", 'scores': [5,5,2,3,5]}, 
{'school_class': "4b", 'scores': [2,2,3]}, 
{'school_class': "4c", 'scores': [3,5,5,3]} 
]

total_score_school = 0
iterrator = 0

for one_class in list_of_pupils:
    average_class = round(sum(one_class["scores"])/len(one_class["scores"]),2)
    print("Средний балл в классе",one_class["school_class"],"-",average_class)
    for pupils in one_class["scores"]:
        total_score_school += pupils
        iterrator += 1
        print(pupils)

average_school = round(total_score_school/iterrator,2)
print("Средний балл по школе",average_school)
