'''
2.5

def main():
    subtotal, gratuityRate = eval( input( "Enter the subtotal and a gratuity rate:"))
    gratuity = subtotal * gratuityRate / 100
    total = subtotal + gratuity
    print ("The gratuity is", gratuity, "and the total is", total)

main()

2.7

def main():
    minutes = eval (input ("Enter the number of minutes:"))
    years = minutes // (60 * 24 * 365)
    daysRemain = (minutes % (60 * 24 * 365) // (60 * 24))
    
    print (minutes, "minutes is approximately", years, "years and", daysRemain, "days")
main()

2.9

def main():
  temp = eval (input ("Enter the temperature in Fahrenheit between -51 and 41:"))
  v = eval (input ("Enter the wind speed in miles per hour: "))
  wc = 35.74 + 0.6215 * temp - 35.75 * v ** 0.16  + 0.4275 * temp * v**0.16
  print ("The wind chill index is", wc)

main()

2.11

def main():
    finalAccountValue = eval (input ("Enter final account value: "))
    annualInterestRate = eval (input ("Enter annual interest rate in percent: "))
    numYears = eval (input ("Enter number of years: "))
    initialDepositAmount = finalAccountValue / ((1 + annualInterestRate / 12 / 100) ** (numYears * 12))
    print ("Initial deposit value is: ", initialDepositAmount)

main()


def main():
    integer1 = eval (input ("Enter an integer: "))
    print (integer1 // 1000)
    integer2 = integer1 - (integer1 // 1000 * 1000)
    print (integer2 // 100)
    integer3 = integer2 - (integer2 // 100 * 100)
    print (integer3 // 10)
    integer4 = integer3 - (integer3 // 10 * 10)
    print (integer4)

main()
'''

def main():
    integer1 = eval (input ("Enter an integer: "))
    integer2 = integer1 - (integer1 // 1000 * 1000)
    integer3 = integer2 - (integer2 // 100 * 100)
    integer4 = integer3 - (integer3 // 10 * 10)
    print (integer4)
    print (integer3 // 10)
    print (integer2 // 100)
    print (integer1 // 1000)

main()
    
    
