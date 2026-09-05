#Arithmetic operators
a = 10
b = 5

print("Addition:", a +  b)
print("Subtraction:", a  - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Reminder:", a % b)
print("Power:", a ** b)

#Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter your second number: "))

print("Addition:", a + b)
print("Subtration:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks calculator
name = input("Enter student name: ")

m1 = int(input("Enter python marks: "))
m2 = int(input("Enter Java marks: "))
m3 = int(input("Enter SQL marks: "))

total = m1 + m2 + m3
average = total / 3

print("\n----- Student Report -----")
print("Name:", name)
print("Total:", total)

#Shopping bill calculator
price1 = float(input("Enter product 1 price: "))
price2 = float(input("Enter product 2 price: "))
price3 = float(input("Enter product 3 price: "))
total = price1 + price2 + price3

#assinment operators
x = 10

x += 5
print(x)

x -= 2
print(x)


x *= 3
print(x)

#bank balance
balance = 10000

deposite = 5000
balance -= deposite

print("After deposite:", balance)

#Comparision operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age ability checker
age = int(input("Enter your age"))

print("Eligibility:", age >=18)
#pass or fail checker
marks = int(input("Enter marks:"))

print("passed:", marks >=40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username")
password = input("Enter password")

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True

print(age >=18 and citizen == True)

age = 16
citizen = True 

print(age >=18 and citizen == True)
has_card = False
has_cash = True

print(has_card or has_cash)
is_logged_in = True

print(not is_logged_in)

#atm eligible checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#Student Scholarship eligibility
marks = float(input("Enter marks: "))
attendence =float(input("Enter attendence: "))

eligible = marks >= 85 and attendence >= 75

print("Scholarship Eligibility:",eligible)