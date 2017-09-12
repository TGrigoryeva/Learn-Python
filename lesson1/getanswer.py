user_question = input("Напиши что-нибудь: ").lower()

def get_answer(question):
    answers={
    "привет":"И тебе привет!",
    "как дела":"Лучше всех", # в юпитере нет ошибки с этим ключом, в cmd есть
    "пока":"Увидимся"
    }
    return answers[question]

print(get_answer(user_question))