'''
def main():
    a, b, c, d, e, f = eval( input( "Enter a, b, c, d, e, f: "))
    if (a * d - b * c) == 0:
        print ("The equation has no solution")
    else:
        x = ((e * d - b * f) / (a * d - b * c))
        y = ((a * f - e * c) / (a * d - b * c))
        print ("x is", x, "and y is", y)

main()

def main():
    date = eval( input("Enter today's day: "))
    days = eval (input("Enter the number of days elapsed since today: "))
    futuredate = date + days
    
    if date % 7 == 0:
        date = "Sunday"
    elif date % 7 == 1:
        date = "Monday"
    elif date % 7 == 2:
        date = "Tuesday"
    elif date % 7 == 3:
        date = "Wednesday"
    elif date % 7 == 4:
        date = "Thursday"
    elif date % 7 == 5:
        date = "Friday"
    elif date % 7 == 6:
        date = "Saturday"

    if futuredate % 7 == 0:
        futuredate = "Sunday"
    elif futuredate % 7 == 1:
        futuredate = "Monday"
    elif futuredate % 7 == 2:
        futuredate = "Tuesday"
    elif futuredate % 7 == 3:
        futuredate = "Wednesday"
    elif futuredate % 7 == 4:
        futuredate = "Thursday"
    elif futuredate % 7 == 5:
        futuredate = "Friday"
    elif futuredate % 7 == 6:
        futuredate = "Saturday"
    
    print ("Today is", date, "and the future day is", futuredate)

main()

def main():
    weight1, price1 = eval( input( "Enter weight and price for package 1: "))
    weight2, price2 = eval( input( "Enter weight and price for package 2: "))
    if price1 / weight1 < price2 / weight2:
        print ("Package 1 has the better price.")
    elif price1 / weight1 > price2 / weight2:
        print ("Package 2 has the better price.")
    else:
        print ("Both packages have the same price.")
main()
'''

def main():
    month, year = eval ( input ("Enter the month and year: "))
    if month == 1:
        month = "January"
        day = 31
    elif month == 2:
        month = "February"
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = 29
        else:
            day = 28
    elif month == 3:
        month = "March"
        day = 31
    elif month == 4:
        month = "April"
        day = 30
    elif month == 5:
        month = "May"
        day = 31
    elif month == 6:
        month = "June"
        day = 30
    elif month == 7:
        month = "July"
        day = 31
    elif month == 8:
        month = "August"
        day = 31
    elif month == 9:
        month = "September"
        day = 30
    elif month == 10:
        month = "October"
        day = 31
    elif month == 11:
        month = "November"
        day = 30
    elif month == 12:
        month = "December"
        day = 31

    print (month, year, "has", day, "days")
main()

'''
def main():
    import sys

    status = eval ( input ( "(0-single filer, 1-married jointly,\n" +
                            "2-married separately, 3-head of household)\n" +
                            "Enter the filing status: "))
    income = eval ( input ( "Enter the taxable income "))

    tax = 0

    if status == 0:
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (income - 33950) * 0.25
        elif income <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (82250 - 33950) * 0.25 + (income - 82250) * 0.28
        elif income <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                  (income - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                  (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
    elif status == 1:
        if income <= 16700:
            tax = income * 0.10
        elif income <= 67900:
            tax = 16700 * 0.10 + (income - 16700) * 0.15
        elif income <= 137050:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                  (income - 67900) * 0.25
        elif income <= 208850:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                  (137050 - 67900) * 0.25 + (income - 137050) * 0.28
        elif income <= 372950:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                  (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                  (income - 208850) * 0.33
        else:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                  (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                  (372950 - 208850) * 0.33 + (income - 372950) * 0.35;
    elif status == 2:
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 68525:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (income - 33950) * 0.25
        elif income <= 104425:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (68525 - 33950) * 0.25 + (income - 68525) * 0.28
        elif income <= 186475:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                  (income - 104425) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                  (186475 - 104425) * 0.33 + (income - 186475) * 0.35;
    elif status == 3:
        if income <= 11950:
            tax = income * 0.10
        elif income <= 45500:
            tax = 11950 * 0.10 + (income - 11950) * 0.15
        elif income <= 117450:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                  (income - 45500) * 0.25
        elif income <= 190200:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                  (117450 - 45500) * 0.25 + (income - 117450) * 0.28
        elif income <= 372950:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                  (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                  (income - 190200) * 0.33
        else:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                  (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                  (372950 - 190200) * 0.33 + (income - 372950) * 0.35;
    else:
        print ("Error: invalid status")
        sys.exit()

    print ("Tax is", format(tax, ".2f"))
main()
'''

def main():
        
            
