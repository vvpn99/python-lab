marks = int(input("Enter student's marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")




ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")


y=input("enter text:")
if i.lower() in "aeiou":
        print(i,' is vowel')
elif i.lower()=="bcdfghjklmnpqrstvwxyz" :
        print(i,' is a consontant)
elif i in "1234567890":
       print(i,"is digit")
else:
       print(i,' is a special character')


       
    

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if year <= 0:
    print("Invalid date")
elif month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28

    elif month in [4, 6, 9, 11]:
        max_days = 30

    else:
        max_days = 31

    if day >= 1 and day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")
