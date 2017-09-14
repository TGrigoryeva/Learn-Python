from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import time
import datetime
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)

    if (user_text == "time"):
        user_text = time.ctime()

    update.message.reply_text(user_text)
    
def tell_me_constellation(bot, update):
    planet_text = "Вызван /planet"
    #print(planet_text)
    update.message.reply_text(planet_text)  
    '''
    update - объект со свойствами (message тоже может быть объектом со свойствами, напр. text) и функциями 
    у update.message есть функция reply_text
    '''
    user_text_planet = update.message.text[8:].capitalize() # то, что пользователь ввел до этого\ planet обрезаем

    #print(user_text_planet)

    d = datetime.datetime.now()

    planets=['Mercury','Venus', 'Sun', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


    '''
    getattr(object, 'Attribute') РАВНО object.Attribute
    getattr(ephem, 'Mars') РАВНО ephem.Mars

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
    '''

    if (user_text_planet in planets):
        planet = getattr(ephem, user_text_planet)
        planet = planet(d.strftime("%Y/%m/%d"))

        planet_text = ephem.constellation(planet)[1]

        update.message.reply_text(planet_text)  
        print(planet_text)
        
def wordcount(bot, update):

    wordcount_text = "Вызван /wordcount"
    print("Вызван /wordcount")
    update.message.reply_text(wordcount_text)
    user_text_wordcount = len(update.message.text[10:].split())  
    #print(len(user_text_wordcount.split()), "слова")
     
    update.message.reply_text(str(user_text_wordcount) + " слова")

def calc(bot, update):

    #var.1 - 2 variables calc

    calc_text = "Вызван /calc"
    print("Вызван /calc")
    update.message.reply_text(calc_text)

    custom_keyboard = [["1", "2", "3", "/"], ["4", "5", "6", "*"], ["7", "8", "9", "+"], ["Esc", "0", "=", "-"]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat.id, #добавлен update.message.chat.id
                 text="Custom Keyboard Test", 
                 reply_markup=reply_markup)

    try:
        user_text_calc= update.message.text
        user_text_calc_corr = user_text_calc.lower().replace(" ","")

        if user_text_calc_corr[-1] != "=":
            update.message.reply_text("отсутствует знак \"=\"")
            return 

        action = user_text_calc_corr[5:-1]
        print("ПОСЛЕ РАЗРЕЗАНИЯ В ACTION ЛЕЖИТ", action)

        total = None

        for operation in range(len(action)):

            print("Смотрим на",action[operation])

            if action[operation] == "+":
                nums = list(map(float, action.split("+")))
                total = sum(nums)
                break

            elif action[operation] == "-":
                nums = list(map(float, action.split("-")))
                total = nums[0]-nums[1]
                break

            elif action[operation] == "*":
                nums = list(map(float, action.split("*")))
                total = nums[0]*nums[1]
                break

            elif action[operation] == "/":
                nums = list(map(float, action.split("/")))
                try:
                    total = nums[0]/nums[1]
                    break
                except ZeroDivisionError:
                    update.message.reply_text("На ноль делить нельзя, попробуйте еще раз")
            
        if total == None:
            update.message.reply_text("Пропущен арифметический знак")
        else:
            update.message.reply_text(total)
                
    except (TypeError, ValueError):
        update.message.reply_text("Введено некорректное значение")

def calc2(bot,update):

    calc2_text = "Вызван /calc2"
    print("Вызван /calc2,")
    update.message.reply_text(calc2_text)

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


    user_text_calc = update.message.text
    user_text_calc_corr = user_text_calc.lower().split()
    print(user_text_calc_corr)
    action = []
    list_iter = 0
      
    for word in user_text_calc_corr:
        if word in dict_convert:
            action.insert(list_iter,dict_convert[word])
            list_iter += 1

    total = None
    print(action)

    if action[1] == "+":
        total = action[0] + action[2]

    elif action[1] == "-":

        total = action[0] - action[2]

    elif action[1] == "*":

        total = action[0] * action[2]

    elif action[1] == "/":

        try:
            total = action[0] / action[2]

        except ZeroDivisionError:
            update.message.reply_text("На ноль делить нельзя, попробуйте еще раз")
            return
    elif total == "":
        update.message.reply_text("Введено некорректное значение")

    update.message.reply_text(total)  
    print(action)
    print(bool(total))
    if total == None: # не понимаю, как сделать эту проверку
        update.message.reply_text("Введено некорректное значение")

#var.2 advanced calc. не работает со скобками
'''    
    calc_text = "Вызван /calc"
    print("Вызван /calc")
    update.message.reply_text(calc_text)

    user_text_calc= update.message.text

    try:
        user_text_calc_corr = user_text_calc.lower().replace(" ","")
         parts = user_text_calc_corr.split("+")

        for plus in range(len(parts)):
            if "-" in parts[plus]:
                parts[plus] = user_text_calc_corr_parts[plus].split("-")

        for plus in range(len(parts)):
            parts[plus] = precalculator(parts[plus])

        print(parts)
        result = sum(parts)
    except ValueError:
        result = "Error"
    except ZeroDivisionError:
        result = "Нельзя делить на ноль"
    return result


def precalculator(part):

    if type(part) is str:

        if "*" in part:
            result = 1
            for subpart in part.split("*"):
                result *= precalculator(subpart)
            return result

        elif "/" in part:
            parts = list(map(float, part.split("/"))) #map означает, что для всех частей нужно прогнать функцию float
            result = parts[0]
            for subpart in parts[1:]:
                result /=subpart
                return result

        else:
            return float(part)

    elif type(part) is list:
        for i in range(len(part))
            part[i] = precalculator(part[i]) # рекурсия,т.е. функция вызывает саму себя
        return part[0] - sum(part[1:])

    return part

'''

def main():
    updater = Updater("391815648:AAE0qLcbOCSna_pE5y1wNqpT302FaKgu3pc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", tell_me_constellation))
    dp.add_handler(CommandHandler("calc", calc)) #25*25=
    dp.add_handler(CommandHandler("calc2", calc2)) #со словарным вводом от 1 до 10
    dp.add_handler(CommandHandler("wordcount", wordcount))

    updater.start_polling()
    updater.idle()

main()

