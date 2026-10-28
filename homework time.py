import datetime

# твій код
date_time = datetime.datetime(2026, 4, 4, 9, 1, 24,585)
print(f"Date Time: {date_time}")
print(f"Type - {type(date_time)}")

OnlyData = date_time.date()
print(f"OnlyData - {OnlyData}")
print(f"Type - {type(OnlyData)}")

OnlyTime = date_time.time()
print(f"OnlyTime - {OnlyTime}")
print(f"Type - {type(OnlyTime)}")

OnlyDate1 = datetime.date(year=2024, month=3, day=4)
OnlyTime1 = datetime.time(hour=23, minute=59)

print(f"date = {OnlyDate1}, type date = {type(OnlyDate1)}")
print(f"time = {OnlyTime1}, type time = {type(OnlyTime1)}")

day = int(input("Введи день: "))
month = int(input("Введи місяць: "))

current_year = datetime.datetime.now().year

print(f"\nDate: {day:02}.{month:02}")

for i in range(20):
    year = current_year + i
    try:
        date = datetime.date(year, month, day)
        day_name = date.strftime("%A")
        print(f"{date.strftime('%d.%m.%Y')} - {day_name}")
    except ValueError:
        print(f"{day:02}.{month:02}.{year} - Немає такої дати")