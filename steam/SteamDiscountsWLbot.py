from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
import logging
from SteamDiscountsWLbot_APIkey import key
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import steam_parser

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    '''
    keyboard = types.InlineKeyboardMarkup()  # С помощью types.ReplyKeyboardMarkup() мы создаём объект нашей будущей клавиатуры, в скобках прописываются нужные параметры. 
    
    wishlist_button = types.InlineKeyboardButton(text="Посмотреть wishlist", callback_data="https://ya.ru")
    notify_button = types.InlineKeyboardButton(text="Подписаться на уведомления", callback_data="https://ya.ru")
    keyboard.add(wishlist_button)  # мы добавляем кнопки в нашу клавиатуру. 
    bot.send_message(message.chat.id, "Узнавайте о скидках на игры из Вашего вишлиста Steam с помощью уведомлений.
    \nИспользуйте \\/off, чтобы приостановить подписку.", reply_markup=keyboard)  # Последнее, что нужно сделать — привязать нашу клавиатуру к нужному сообщению, делается это при помощи параметра reply_markup в любом методе send_...
    '''
    keyboard = [[InlineKeyboardButton("Посмотреть wishlist", callback_data='wishlist'),
                 InlineKeyboardButton("Подписаться", callback_data='notification')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Узнавайте о скидках на игры из Вашего вишлиста Steam с помощью уведомлений.\nИспользуйте /off, чтобы приостановить подписку.", 
        reply_markup=reply_markup)  # клавиатура появится сразу после этого сообщения

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)

    if (user_text == "time"):
        user_text = time.ctime()

    update.message.reply_text(user_text)
    
def button(bot, update):
    query = update.callback_query  # в query лежит здоровый словарь, в data e лежит callback_data
    print(query)
    bot.editMessageText(text="Selected option: %s" % query.data,  # для изменения сообщения
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    if query.data == 'wishlist':
        steam_parser.wishlist_notifications("naash71")

def main():
    updater = Updater(key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the Bot
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

main()

