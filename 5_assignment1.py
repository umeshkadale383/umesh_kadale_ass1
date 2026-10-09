# 1.  Check if a number is positive, negative, or zero. 
# num=int(input("enter number:"))

# if num>=0:
#     print("number is positive")
# elif num<1:
#     print("number is negetive")
# else:
#     print("number is zero")

# 2.  Check whether a number is even or odd. 

# num=int(input("enter a number:"))

# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")


# 3.  Find the greater of two numbers. 
# num1=int(input("enter 1 number:"))
# num2=int(input("enter 2 number:"))

# if num1>num2:
#     print("first number is greater")
# else:
#     print("second number is lesser")

# 4.  Find the greatest of three numbers. 
# num1=int(input("enter 1 number:"))
# num2=int(input("enter 2 number:"))
# num3=int(input("enter 3 number"))

# if num1>num2:
#     print("first is greater")
# elif num2>num3:
#     print("second is greater")
# else:
#     print("third is greater")

# 5.  Check if a person is eligible to vote (age ≥ 18).

# adharcard=input("do you have adhar card")
# age=int(input("enter your age"))

# if age>=18 and adharcard=="yes":
#     print("you are able to vote")
# else:
#     print("you cant vote")

# 6.  Check whether a year is a leap year.

# y = int(input("enter year"))

# if y % 4 == 0:
    
#     if y % 100 == 0:
#         if y % 400 == 0:
            
#             print("Leap year") 
#         else:
#             print("Not a leap year")  
#     else:
#         print("Leap year") 
# else:
#     print("Not a leap year")

# 7.  Check if a character is a vowel or consonant. 

# char=str(input("enter character"))

# if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#     print("entered char are vowel")
# else:
#     print("entered char are consonant")

# 8.  Check whether a number is divisible by 5 and 11. 

# num=int(input("enter a number"))

# if num%5==0 and num%11==0:
#     print("number is divisible")
# else:
#     print("number not divisible")

# 9.  Check if a number is a multiple of both 3 and 7. 



# 10.  Assign grades based on marks: 
# a.  90–100: A 
# b.  80–89: B 
# c.  70–79: C 
# d.  60–69: D 
# e.  Below 60: F 

# mks=int(input("enter mks"))

# if mks>90 and mks<100:
#     print("A")
# elif mks>80 and mks<89:
#     print("B")
# elif mks>70:
#     print("C")
# elif mks>60:
#     print("D")
# elif mks<60:
#     print("F")

# 11.  Check if a character is uppercase or lowercase.

# ch=input("enter character")
# if 65 <= ord(ch) <= 90:
#     print("Uppercase")
# elif 97 <= ord(ch) <= 122:
#     print("Lowercase")
# else:
#     print("Not a letter")

# 12.  Find whether the entered alphabet is a vowel using if-elif.

# alph=input("enter alphabet:")

# if alph=="a":
#     print("vowel")
# elif alph=="e":
#     print("vowel")
# elif alph=="i":
#     print("vowel")
# elif alph=="o":
#     print("vowel")
# elif alph=="u":
#     print("vowel")
# else:
#     print("consonant")

#  13--not solvable


# 14.  Determine the type of triangle (Equilateral, Isosceles, Scalene). 



# 15.  Find the largest among four numbers. 

# n1=int(input("enter 1 number"))
# n2=int(input("enter 2 number"))
# n3=int(input("enter 3 number"))
# n4=int(input("enter 4 number"))

# if n1>n2:
#     print("n1 is largest")
# elif n2>n3:
#     print("n2 is largest")
# elif n3>n4:
#     print("n3 is largest")
# else:
#     print("n4 is largest")


# 16.  Check whether a number is a three-digit number.

# digit=int(input("enter digits"))

# if digit>=999 or digit>99:
#     print("number is three digit")
# else:
#     print("number not three digit")

# 17.  Calculate electricity bill using slab rates. 

# unit=int(input("enter you consumed units"))
# rate=20

# if unit>=20:
#     print("your bill will be:",unit*rate)
# elif unit>=40:
#     print("your bill will be: ",unit*rate)
# else:
#     print("no bill get")


# 18.  Calculate income tax based on income slabs. 

# income=int(input("enter your salary"))

# if income>100000:
#     print("you are in 30 percent slab")
# elif income>15000 and income<=50000:
#     print("from your salary 10 percent will deducted")
# elif income>51000 and income<=100000:
#     print("you are in 20 percent salary slab")
# else:
#     print("your salary are low thats why you not get any money deduction")

# 19.  Check if a student passes (minimum 35 marks in each subject). 

# s1=int(input("enter your mks:"))
# s2=int(input("enter your mks:"))
# s3=int(input("enter your mks:"))

# if s1>=35 and s2>=35 and s3>=35:
#     print("congratulation! you are passed")
# else:
#     print("failure is the part of life")

# 20.  Find whether a number is within a given range. 

# num=int(input("enter your number"))

# if num >=0 and num<=100:
#     print("you are in range of 0-100")
# elif num>=101 and num<=1000:
#     print("you are in range of 101-1000")
# else:
#     print("you are in out of range")

# 21.  Build a simple calculator using if-elif-else (+, -, *, /). 
# a = float(input("Enter number 1: "))
# b = float(input("Enter number 2: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Division")
# print("4. Multiplication")

# choice = int(input("Enter your choice (1-4): "))

# if choice == 1:
#     print("Addition will be", a + b)

# elif choice == 2:
#     print("Subtraction will be", a - b)

# elif choice == 3:
#     if b != 0:
#         print("Division will be", a / b)
#     else:
#         print("Cannot divide by zero")

# elif choice == 4:
#     print("Multiplication will be", a * b)

# else:
#     print("Invalid choice")


# 22.  Check if a year is a century leap year. 

# year = int(input("Enter year: "))

# if year % 100 == 0 and year % 400 == 0:
#     print("Century Leap Year")
# elif year % 100 == 0:
#     print("Century Year but not Leap Year")
# elif year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# 23.  Determine the season based on the month number

# month = int(input("Enter month number (1-12): "))

# if month in [3, 4, 5]:
#     print("Summer")
# elif month in [6, 7, 8, 9]:
#     print("Rainy Season")
# elif month in [10, 11]:
#     print("Autumn")
# elif month in [12, 1, 2]:
#     print("Winter")
# else:
#     print("Invalid Month")

# 24.  Find the number of days in a month. 
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 Days")
# elif month in [4, 6, 9, 11]:
#     print("30 Days")
# elif month == 2:
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         print("29 Days")
#     else:
#         print("28 Days")
# else:
#     print("Invalid Month")

# 25.  Check whether a password meets minimum conditions (length, digits, etc.).

# password = input("Enter password: ")

# if len(password) >= 8 and any(c.isdigit() for c in password):
#     print("Valid Password")
# else:
#     print("Invalid Password")

# 26.  Determine ticket price based on age category. 
# age = int(input("Enter age: "))

# if age < 5:
#     print("Ticket is Free")
# elif age <= 12:
#     print("Ticket Price: Rs. 50")
# elif age <= 59:
#     print("Ticket Price: Rs. 100")
# else:
#     print("Ticket Price: Rs. 60")

# 27.  Calculate discount based on purchase amount.
# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = amount * 0.20
# elif amount >= 2000:
#     discount = amount * 0.10
# elif amount >= 1000:
#     discount = amount * 0.05
# else:
#     discount = 0

# print("Discount:", discount)
# print("Final Amount:", amount - discount)

# 28.  Check if a person is eligible for a driving license (age and eyesight condition). 
# age = int(input("Enter age: "))
# eyesight = input("Is eyesight normal? (yes/no): ")

# if age >= 18 and eyesight == "yes":
#     print("Eligible for Driving License")
# else:
#     print("Not Eligible")

# 29.  Create a login system with username and password validation. 
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Invalid Username or Password")

# 30.  Create a menu-driven program using if-elif-else with options like: 
# a.  Addition 
# b.  Subtraction 
# c.  Multiplication 
# d.  Division 
# e.  Exit 

# while True:
#     print("\n1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 5:
#         print("Thank You!")
#         break

#     elif choice in [1, 2, 3, 4]:
#         a = float(input("Enter number 1: "))
#         b = float(input("Enter number 2: "))

#         if choice == 1:
#             print("Addition:", a + b)
#         elif choice == 2:
#             print("Subtraction:", a - b)
#         elif choice == 3:
#             print("Multiplication:", a * b)
#         elif choice == 4:
#             if b != 0:
#                 print("Division:", a / b)
#             else:
#                 print("Cannot divide by zero")
#     else:
#         print("Invalid Choice")