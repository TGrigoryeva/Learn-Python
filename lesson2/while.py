#task 1
list_of_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 
while True:
    name = list_of_names.pop() # функция pop выполняет 2 действия: возвращает последний или указанный элемент списка, а затем удаляет его из списка
    print("Текущее имя:", name)
    if (name == "Валера"):
        print("Валера нашелся!")
        break

#task 2
list_of_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 

def find_person(names):
    while True:
        name = names.pop()
        print("Текущее имя: ", name)
        if name == "Валера":
            print("Валера нашелся!")
            break

find_person(list_of_names)



#task 3
def ask_user(): 
    while True:
        answer = str.lower(input("Как дела? "))
        if answer == "хорошо":
            print("Ну и зашибись")
            break
ask_user()


#task 4 
import datetime;

get_answer_dict = {"привет!": "Привет!", "как дела?": "Отлично!", "в чем смысл жизни?": "Смысла нет", "время": datetime.datetime.now()}

def get_answer(question):
   return print(get_answer_dict.get(question))
 

def ask_user1(): 
    try:  
        while True:
            question = str.lower(input("Напиши что-нибудь: "))
            if question == "пока":
                print("Пока!")
                break
            else:
                get_answer(question)    
    except KeyboardInterrupt: #task 2 "exceptions"
        return

ask_user1()
