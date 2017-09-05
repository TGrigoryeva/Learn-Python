mylist = [10,20,30,40,50,60,70,80,90,100] #task 1
for score in mylist:
    print(score+1)


user_input=input("Введите любу строку: ") #task 2
for characters in user_input:
    print(characters)


list_of_pupils=[ {'school_class': "4a", 'scores': [5,5,2,3]}, {'school_class': "4b", 'scores': [2,2,2,3]}, {'school_class': "4c", 'scores': [3,5,5,3]} ] #task 3
total_score_school = 0
for dictionary in list_of_pupils:
    average_class = sum(dictionary["scores"])/len(dictionary["scores"])
    total_score_school += average_class
    print(dictionary["school_class"],"-",average_class)
average_school = total_score_school/len(list_of_pupils)

print("Average score: ",average_school)
