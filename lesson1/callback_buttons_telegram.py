def greet_user(bot, update):

    keyboard = [[InlineKeyboardButton("Посмотреть wishlist", callback_data='wishlist'),
                 InlineKeyboardButton("Подписаться", callback_data='notification')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Для просмотра вишлиста и получения уведомлений о скидках из вишлиста введите юзернейм из персональной ссылки Steam\nhttр://steamcommunity.cоm/id/username\n и нажмите на кнопку внизу\n\nЛибо отправьте команду в формате:\n/wishlist username\n/notification username\n\nИспользуйте /off, чтобы приостановить подписку.", 
reply_markup=reply_markup, parse_mode = telegram.ParseMode.MARKDOWN) # клавиатура появится сразу после этого сообщения

def button(bot, update):
    query = update.callback_query  # в query лежит здоровый словарь, в data лежит callback_data
    print(query)
    bot.editMessageText(text="Selected option: %s" % query.data,  # для изменения сообщения
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    if query.data == 'wishlist':
        wishlist_notifications("naash71",query.data)
