def math_statement(user_input):

    dict_convert = {
    "ноль":0,
    "один":1,
    "два":2,
    "три":3,
    "четыре":4,
    "пять":5,
    "шесть":6,
    "семь":7,
    "восемь":8,
    "девять":9,
    "десять":10,
    "умножить":"*",
    "минус":"-",
    "плюс":"+",
    "разделить":"/"
    }

    user_input = input("Введите математическое выражение:").lower()
    user_input_list = user_input.split()

    user_input_list_math_st = []
    list_iter = 0
      
    for word in user_input_list:
        if word in dict_convert:
            user_input_list_math_st.insert(list_iter,dict_convert[word])
            list_iter += 1

    return user_input_list_math_st #сколько будет три минус два превращается в [3, '-', 2]

 print(math_statement(user_input_list_math_st))