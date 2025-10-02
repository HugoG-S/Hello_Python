### Dates ###

from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()

def print_date(date):
    print(date.day, "/", date.month, "/", date.year)
    print("Hora: ", date.hour, ":", date.minute, ":" , date.second)
    print(date.timestamp())

print(now.hour)
print(now.day)
print(now.minute)
print(now.year)
print(now.second)
print(now.month)

print("Hora: ", now.hour, ":", now.minute, ":" , now.second)



print(timestamp)

print_date(now)

print(now.day, "/", now.month, "/", now.year)

year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

# con .today automaticamente pone la fecha actual de cuando se ejecuta

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2025, 11, 8)

print(current_date.day)
print(current_date.month)
print(current_date.year)

## Podemos hacer operaciones:

current_date = date(current_date.year + 2, current_date.month, current_date.day)

print(current_date.year)

diff = year_2025 - now
print(diff)
diff = year_2025.date() - current_date
print(diff)

## TimeDelta nos deja trabajar con franjas de tiempo

from datetime import timedelta

star_delta = timedelta(200, 100, 100, weeks = 10)
end_delta = timedelta(300, 100, 100, weeks = 13)

print(end_delta - star_delta)
print(end_delta + star_delta)
