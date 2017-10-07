from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
import logging
from SteamDiscountsWLbot_APIkey import key
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from steam_parser import wishlist_notifications, check_username
import re
from steam_db import db_session, Chat

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    update.message.reply_text("Для просмотра вишлиста отправьте сообщение с юзернеймом из персональной ссылки Steam\nhttр://steamcommunity.cоm/id/username\n\nДля подписки на уведомления отправьте команду в формате:\n /notification username\n\nИспользуйте /off, чтобы приостановить подписку.") # клавиатура появится сразу после этого сообщения

def talk_to_me(bot, update):
    user_text = update.message.text # устранить ошибки с пробелами. с большими буквами ошибки не будет
    print(user_text)
    if check_username(user_text) is False:
        update.message.reply_text("Пользователя {} не существует, либо страница скрыта".format(user_text))
    else:
        my_data = wishlist_notifications(user_text,"wishlist")  # тут словарь лежит
        print(my_data)
        for key,value in my_data.items():
                print(value)
                update.message.reply_text(value)
        
def notification(bot, update):
    user_text = update.message.text[13:].replace(" ","")   
    if check_username(user_text) is False:
        update.message.reply_text("Пользователя {} не существует, либо страница скрыта".format(user_text))
    else:
        tel_chat_id = update['message']['chat']['id']
        print(tel_chat_id)
        db_tel_chat_id = Chat.query.filter(Chat.chat_id == tel_chat_id).first()
        print(db_tel_chat_id)
        if db_tel_chat_id is None:
            db_session.add(Chat(tel_chat_id, True, user_text))
            db_session.commit()
            update.message.reply_text("Подписка включена")
        else:
            update.message.reply_text("Для новой подписки отмените предыдущую")

def off(bot, update):
    tel_chat_id = update['message']['chat']['id']    
    try:
        row_to_delete = db_session.query(Chat).filter(Chat.chat_id == tel_chat_id).first()
        db_session.delete(row_to_delete)
        update.message.reply_text("Подписка отключена")
    except:
        update.message.reply_text("Что-то пошло не так")
    db_session.commit()

def main():
    updater = Updater(key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("notification", notification))
    dp.add_handler(CommandHandler("off", off))
#    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the Bot
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

main()

