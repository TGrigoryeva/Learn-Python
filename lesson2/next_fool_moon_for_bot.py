'''
Полнолуние
Научить бота отвечать на вопрос “Когда ближайшее полнолуние после 2016-10-01?”. 
Чтобы узнать, когда ближайшее полнолуние, используй модуль ephem. 
Чтобы им пользоваться, его нужно установить ($ pip install ephem) и импортировать. 
'''
import ephem
import re
from datetime import datetime, date

when_next_fool_moon_question = "Когда ближайшее полнолуние после 2016-10-01"

find_date_in_next_fool_moon_question = re.findall(r'\d{4}-\d{2}-\d{2}' , when_next_fool_moon_question)
find_date_in_next_fool_moon_question_String = ''.join(find_date_in_next_fool_moon_question).replace("-","/")


next_fool_moon_date = datetime.strptime(find_date_in_next_fool_moon_question_String, "%Y/%d/%m")
print(ephem.next_full_moon(next_fool_moon_date))


