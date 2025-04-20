#⚠️ What is Exception Handling?
#Exception ka matlab hai koi error jo program chalte waqt aati hai.
#Python mein exception handling ka matlab hai:
#“Error aaye to program crash na ho, balki handle ho jaye.”

#🧰 Try, Except, Else, Finally
#Python mein hum try, except, else, aur finally ka use karke error ko handle karte hain.

#🔹 1. Basic Try-Except Example
try:
    x = int(input("Ek number daaliye: "))
    print("Aapka number hai:", x)
except ValueError:
    print("Error: Sirf number daaliye!")
 #Agar user number ke bajaye koi string daal de, to ValueError aayega. except usko pakad lega aur program crash nahi hoga.

#🔸 2. Try-Except-Else
try:
    num = int(input("Number daaliye: "))
except ValueError:
    print("Invalid input!")
else:
    print("Shukriya! Aapka number:", num)
#✅ else tab chalta hai jab koi error na aaye.

#🔹 3. Try-Finally
try:
    print("Program shuru ho gaya")
    result = 10 / 0
except ZeroDivisionError:
    print("Error: 0 se divide nahi ho sakta")
finally:
    print("Yeh block hamesha chalega")
    #✅ finally block hamesha chalta hai — chahe error aaye ya na aaye.

#🔸 4. Catching Multiple Exceptions
try:
    num = int(input("Number daaliye: "))
    print(10 / num)
except ValueError:
    print("Number sahi nahi diya!")
except ZeroDivisionError:
    print("0 se divide nahi ho sakta!")









