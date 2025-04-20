#📐 1. math Module – (Maths wale kaam ke liye)
#Python ka math module basic aur advanced maths functions provide karta hai.

import math

print(math.sqrt(25))       # 5.0
print(math.factorial(5))   # 120
print(math.pow(2, 3))      # 8.0
print(math.ceil(2.3))      # 3
print(math.floor(2.7))     # 2
print(math.pi)             # 3.141592653589793

#📌 Useful Functions:
#Function | Kaam
#sqrt(x) | Square root
#factorial(x) | x!
#pow(x, y) | x^y
#ceil(x) | Oopar wala number
#floor(x) | Neeche wala number
#pi | 3.14...

#🕰️ 2. datetime Module – (Date aur Time ka kaam)
#Python ka datetime module se hum date/time get, format, compare kar sakte hain.
import datetime

now = datetime.datetime.now()
print("Aaj ki tareekh:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

#🔸 Custom Date Banana:
birthday = datetime.date(2000, 5, 15)
print("Birthday:", birthday)

#🔸 Full Year Calendar:
#print(calendar.calendar(2025))

#🔹 Check if Leap Year:
#print(calendar.isleap(2024))   # True
#print(calendar.isleap(2025))   # False



