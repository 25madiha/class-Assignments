#📂 What is File Handling?
#File handling ka matlab hai Python ka use karke files read (padhna), write (likhna), aur modify karna.

#Python mein file handling ka kaam open() function se hota hai.

file = open("demo.txt", "w")
file.write("Yeh mera pehla file hai!\n")
file.write("Python file handling is easy.")
file.close()
#Agar demo.txt file exist nahi karta, to yeh create ho jayega.
#write() se hum content likhte hain.
#close() se file band karte hain.

#🔸 2. Read from a File
file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()
#📌 Tip: Agar file exist nahi karti, to r mode mein error aayega.


#🔹 3. Append to a File
file = open("demo.txt", "a")
file.write("\nYeh line baad mein add ki gayi hai.")
file.close()
#✅ Ismein existing file ke content ko delete nahi karta — sirf aakhir mein naya text add hota hai.

#🔸 4. Read Line-by-Line
file = open("demo.txt", "r")
for line in file:
    print(line.strip())
file.close()
#strip() extra newline hata deta hai.

#🔹 5. With Statement (Best Practice)
with open("demo.txt", "r") as file:
    print(file.read())
#✅ with block automatically file ko close kar deta hai — safe & clean code.





