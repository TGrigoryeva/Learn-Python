from datetime import datetime, date, timedelta
from monthdelta import monthdelta #pip install monthdelta  #если загрузить модуль, а не метод из модуля как в данном случае, придется писать  monthdelta.monthdelta(!)

import locale #для даты прописью на русском
   
    #Напечатайте в консоль даты: вчера, сегодня, месяц назад timedelta
date_today = date.today()
print("Сегодня", date_today.strftime("%d.%m.%Y")) #strftime - дату сохранить как строку, strptime - наоборот
#date_today.strftime("%d.%m.%Y") - по идее, вывод на печать может быть и без print

delta_day = timedelta(days = 1) # class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
yesterday = date_today - delta_day
print("Вчера", yesterday.strftime("%d.%m.%Y"))

#delta_m = monthdelta(months = 1)
month_ago =  date_today - monthdelta(1) #если загрузить модуль, а не метод из модуля как в данном случае, придется писать  monthdelta.monthdelta(!)
print("Месяц назад", month_ago.strftime("%d.%m.%Y"))

    #Превратите строку "01/01/17 12:10:03.234567" в объект datetime
date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f") #strftime - дату сохранить как строку, strptime - наоборот
print("Превратили строку в объект datetime:",date_dt)