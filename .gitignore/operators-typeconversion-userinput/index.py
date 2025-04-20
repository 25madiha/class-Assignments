""""
# operation in python
# Arithemetic operators

print(2+3) #Addition
print(2-3) #subtraction
print( 2*3) #Multiplication
print(2/3) #Division
print(2**3)#Exponentation 2 ki power 3 yani 2*2*2
print(3%2)#Modules

# Comparison operators or Relational operator

print(2==3) #Equal to
print(2!=3) #Not equal to
print(2<3)  #Less than
print(2<=3) #Less than or equal to
print(2>3)  #Greater than

print(2>=3) #Greater than or equal to
"""""
"""""
# Logical operators
a=2 
b=3 
print(a<b and b>a)
# print(True and True) #AND
print(a>b and b>a)

print(True and False) #AND


print(True or False) #OR is m phli wali condition dkhi jati hai agr wo true hai tw true hi ayega agr false hai tw false hi

print(False or False) #OR

print(not False) #NOT condition chage krdeta hai (not true ) hoga tw false ayega (not false hga tw true ayega)


print(not True) #NOT
"""""
"""""
# Assignment operators

a = 10

a += 10
 

print(a)

b = 10

b -= 10

print(b)

c = 10 

c *= 10

print(c)

d = 10

d /= 10

print(d)

e = 10

e **= 10

print(e)

f = 10

f %= 10

print(f)

"""""
"""
#  type conversion

a = 10 

print(type(a))

b = str(a)

print(type(b))

c= float(a+5)

print(type(c))

"""
# User Input

# a=input("enter your first value")

# b=input("enter your second value")

# print(int(a)+int(b))

#a= input("enter name:")


#print(a)

# type comparision operator 
a = 5
b = 5
print(a == b)  # True equal equal to 

a = 5
b = 3
print(a != b)  # True not equal to

a = 7
b = 4
print(a > b)  # True greater than

a = 2
b = 5
print(a < b)  # True less than 

a = 5
b = 5
print(a >= b)  # True greater than equal to

a = 3
b = 7
print(a <= b)  # True less than equal to 

# Identity operators
# Python mein identity operator check karta hai ke do variables ek hi memory location ko refer karte hain ya nahi.
#example : "Ali aur Ahmed dono ek hi kitaab ko dekh rahe hain" → is → True
#"Ali aur Sana ke paas alag alag kitaabein hain, lekin dono mein same content hai" → == True, lekin is False

#Returns True if both variables point to the same object.
#IS
a = [1, 2, 3]
b = a
print(a is b)  # True — because both point to the same list object in memory

#IS NOT
#Returns True if the variables do not point to the same object.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # True — because they are two different objects, even though their contents are equal

#Membersship oprators
#Membership operators are used to check if a value exists in a sequence (like a list, tuple, string, or set).
#There are two membership operators:

#IN 
#Returns True if the value is found in the sequence.

fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)   # True
print('mango' in fruits)    # False

#NOT IN
text = "hello world"
print("world" in text)      # True
print("bye" in text)        # False

# NOT IN
#Returns True if the value is not found in the sequence.
numbers = [1, 2, 3, 4]
print(5 not in numbers)     # True
print(3 not in numbers)     # False

 #Example with if statement
name = "Alice"
if "A" in name:
    print("The name starts with A!")

    #BITWISE OPERATOR 
    #Bitwise operators are used to perform bit-level operations on integers. They work directly on the binary representations of numbers.

#BITWISE (AND)
#Returns 1 if both bits are 1.
a = 5       # 0101
b = 3       # 0011
print(a & b)  # 1 => 0001

# BITWISE | OR
#Returns 1 if either bit is 1.
print(a | b)  # 7 => 0111

#BITWISE (XOR)
x = 5        # 0101
print(~x)    # -6 => In binary: 1010 (inverted 0101), which is -6 in two’s complement

#BITWISE NOT
#Inverts all bits (i.e., 1 becomes 0, and vice versa). In Python, this gives the result as -x - 1.
x = 5        # 0101
print(~x)    # -6 => In binary: 1010 (inverted 0101), which is -6 in two’s complement

#BITWISE LEFT SHIFT
x = 3        # 0011
print(x << 2)  # 12 => 1100

#RIGHT SHIFT
#Shifts bits to the right by a given number of positions.

x = 8        # 1000
print(x >> 2)  # 2 => 0010



























