list_of_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while True:
    name = list_of_names.pop() # функция pop выполняет 2 действия: возвращает последний или указанный элемент списка, а затем удаляет его из списка
    print("Текущее имя:", name)
    if (name == "Валера"):
        print("Валера нашелся!")
        break


list_of_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(names):
    while True:
        name = names.pop()
        print("Текущее имя: ", name)
        if name == "Валера":
            print("Валера нашелся!")
            break

find_person(list_of_names)


def get_answer():
    while True:
        question = str.lower(input("Какой у Вас вопрос? "))
        if question == "пока":
            break
        else:
            print("Я не знаю ответа на вопрос {}".format(question))

def ask_user():
    while True:
        answer = str.lower(input("Как дела? "))
        get_answer() # я вообще не поняла по условиям задачи, куда впиндюрить эту функцию
        if answer == "хорошо":
            print("Ну и зашибись")
            break
ask_user()