"""
radius = 20
area = radius * radius * 3.14159
print ("The area for the circle of radius", radius, "is", area)

radius = eval(input("Enter a value for radius: "))
area = radius * radius * 3.14159
print ("The area for the circle of radiu", radius, "is", area)

number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second number: "))
number3 = eval(input("Enter the third number: "))
average = (number1 + number2 + number3) / 3
print ("The average of", number1, number2, number3, "is", average)

number1, number2, number3 = eval(input("Enter three numbers separated by commas: "))
average = (number1 + number2 + number3) / 3
print("The average of", number1, number2, number3, "is", average)
   
seconds = eval(input("Enter an integer for seconds: "))
minutes = seconds // 60
remainingSeconds = seconds % 60
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")

purchaseAmount = eval(input("Enter purchase amount: "))
tax = purchaseAmount * 0.06
print("Sales tax is", int(tax *100) / 100.0)

import time
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")

annualInterestRate = eval (input( "Enter annual interest rate, e.g., 7.25: "))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("Enter number of years as an integer, e.g., 5: "))
loanAmount = eval(input("Enter loan amount, e.g., 120000.95: "))
monthlyPayment = loanAmount * monthlyInterestRate / (1 -
        1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12
print ("The monthly payment is", int(monthlyPayment *100) / 100)
print ("The total payment is", int(totalPayment *100) / 100)
"""

x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print("The distance between the two points is", distance)

    
