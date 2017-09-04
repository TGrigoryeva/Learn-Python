def get_answer(question):
    answers={"Привет":"И тебе привет","как дела":"лучше всех","пока":"увидимся"}
    return answers[question]
print(get_answer("как дела"))