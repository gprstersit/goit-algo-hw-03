# Home work #1
###############################################################################################################################
def get_days_from_today(date):
    from datetime import datetime
    try:
        input_date = datetime.strptime(date , '%Y-%m-%d')
        today = datetime.now()
        days_difference = (today - input_date).days
        return days_difference

    except ValueError:
        print("Incorrect date format. Please enter in 'YYYY-MM-DD' format.")


date = input("Enter date in 'YYYY-MM-DD' format: ")
days_difference = get_days_from_today(date)
print("Number of days between the entered date and today:", days_difference)
# ###############################################################################################################################

# Home work #2
###############################################################################################################################
def get_numbers_ticket(min, max, quantity):
    import random
    if min< 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        print('Invalid parameters.')
        return []
    all_numbers = list(range(min, max + 1))
    random_numbers = random.sample(all_numbers, quantity)
    random_numbers.sort()
    return random_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Good luck:", lottery_numbers)
###############################################################################################################################

# Home work #3
###############################################################################################################################
import re

def normalize_phone(phone_number):
    p1=r"[\d\+]+"
    phone_number=''.join(re.findall(p1,phone_number))
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)==12:
        phone_number='+'+phone_number
    return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
###############################################################################################################################

# Home work #4
###############################################################################################################################
import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date() # беремо сьогоднішню дату
    birthdays=[] # створюємо список для результатів
    for user in users: # перебираємо користувачів
        bdate=user["birthday"] # отримуємо дату народження людини у вигляді рядка
        bdate=str(tdate.year)+bdate[4:] # Замінюємо рік на поточний
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
        days_between=(bdate-tdate).days # рахуємо різницю між зараз і днем народження цьогоріч у днях
        if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні
            if week_day<6: #  якщо пн-пт
                birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
                # Додаємо запис у список.
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:# якщо неділя
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
                elif (bdate+dt.timedelta(days=2)).weekday()==0: #якщо субота
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
    return birthdays

print(get_upcoming_birthdays(users))