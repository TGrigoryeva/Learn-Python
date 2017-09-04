from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time

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
    
def main():
    updater = Updater("391815648:AAE0qLcbOCSna_pE5y1wNqpT302FaKgu3pc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

main()

