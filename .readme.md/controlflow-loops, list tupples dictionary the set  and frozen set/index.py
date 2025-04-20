#if,elif, else – (Decision Making)
#Yeh Python ko batata hai ke kis condition par kya karna hai.

age = 18

if age >= 18:
    print("Aap vote de sakte hain")
else:
    print("Aap abhi chhote hain")

    #ELIF (extra condition)
    marks = 75

if marks >= 90:
    print("A+ Grade")
elif marks >= 70:
    print("A Grade")
else:
    print("Improve karo")

    #🔁 Loops (Repeat karna koi kaam)
    #🔹 3. while loop – Jab tak condition true ho, tab tak repeat
i = 1

while i <= 5:
    print("Number:", i)
    i += 1
    
    #🔸 4. for loop – List ya range ke liye loop
for name in ["Ali", "Sara", "Ahmed"]:
    print("Hello", name)

    #🔹 5. range() ke saath for loop
for i in range(1, 6):
    print(i)

#🔸 6. break – Loop ko beech mein todna
for i in range(1, 10):
    if i == 5:
        break
    print(i)

    #🔹 7. continue – Ek iteration skip karna
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

    #lesson 6 list tupples dictionary

    #📦 1. List – (Cheezon ki ordered list jo badal sakti hai)
    #List ek aisi container hai jo multiple items ko store karti hai. Isme hum value ko add, remove ya change kar sakte hain.
fruits = ["apple", "banana", "mango"]
print(fruits[0])         # Output: apple

fruits[1] = "orange"     # banana ko orange se replace kar diya
print(fruits)            # ['apple', 'orange', 'mango']

#📦 2. Tuple – (List jaisi hi hoti hai, lekin change nahi hoti)
#Tuple ek fixed list hai. Hum uske elements ko change nahi kar sakte.
colors = ("red", "green", "blue")
print(colors[1])         # Output: green

# colors[1] = "yellow"   ❌ Error – Tuples can't be modified


#📦 3. Dictionary – (Key:Value pair ka collection)
#Dictionary ek aisa structure hai jahan har item ka naam (key) aur value hoti hai. Jaise ek chhoti si database.
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

print(student["name"])       # Output: Ali

student["age"] = 21          # Value change ki
print(student["age"])        # Output: 21

#lesson 7 the set and frozen set

#📦 1. Set – (Unique items ka unordered collection)
#Set ek aisa container hai jo duplicate values ko hata deta hai, aur elements unordered hote hain.

fruits = {"apple", "banana", "mango", "apple"}
print(fruits)  # Output: {'banana', 'mango', 'apple'}  ← Duplicate 'apple' hata diya

#🔹 Set operations:

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union => {1, 2, 3, 4, 5}
print(a & b)   # Intersection => {3}
print(a - b)   # Difference => {1, 2}

# frozen set (immutable set)
#Frozen set ek unchangeable version hoti hai set ki. Aap usme value add/remove nahi kar sakte.

numbers = frozenset([1, 2, 3, 4])
print(numbers)

# numbers.add(5)  ❌ Error: 'frozenset' object has no attribute 'add'



























