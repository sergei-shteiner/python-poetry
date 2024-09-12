# а вы знали раньше что тринадцатое 
# выпадает чаще всех на пятницу?
# вот и я когда-то не поверил
# написал программу и проверил

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

days_in_month_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(month, year):
    if month == 2 and is_leap(year):
        return 29
    return days_in_month_non_leap[month - 1]

def next_date(day, month, year):
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

day, month, year = 1, 1, 2001 # это был понедельник
current_day_of_week = 0 # понедельник

loop =  400 * 7 # years
till_year = year + loop # должно хватить

day_of_week_13 = [0, 0, 0, 0, 0, 0, 0]

while True:
    if day == 13:
        day_of_week_13[current_day_of_week] += 1
    day, month, year = next_date(day, month, year)
    current_day_of_week = (current_day_of_week + 1) % 7
    if year == till_year:
        break


days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
for i in range(7):
    print(days_of_week[i], day_of_week_13[i], "раз")