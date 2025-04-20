#📘 Part 1: Functions in Python
#Function ek block hota hai jo specific kaam karta hai. Jise hum baar-baar reuse kar sakte hain.
def greet():
    print("Assalamu Alaikum!")

greet()  # Call the function

# function with parametres
def greet(name):
    print("Hello", name)

greet("Ali")   # Output: Hello Ali

#🔹 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # Output: 8

#🔹 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # Output: 8

#📦 Part 2: Modules in Python
#Module ek file hoti hai jisme Python code likha hota hai (usually functions or variables) jise hum import karke use karte hain.

#🔹 1. Using a Built-in Module
import math

print(math.sqrt(16))   # Output: 4.0
#Yahan math ek module hai, jisme sqrt() function available hai.

#🔸 2. Importing Specific Function
from math import pi

print(pi)  # Output: 3.141592653589793











