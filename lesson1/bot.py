from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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
        

def main():
    updater = Updater("391815648:AAE0qLcbOCSna_pE5y1wNqpT302FaKgu3pc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", tell_me_constellation))

    updater.start_polling()
    updater.idle()

main()

