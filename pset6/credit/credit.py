n = int(input("Number: "))

while (n <= 0):
    n = int(input("Number: "))

countDigits = 0
valid = n

while (valid > 0):
    valid = valid // 10
    countDigits + 1
check1=0
digit1=0
digit2=0
digit3=0
digit4=0
digit5=0
digit6=0
digit7=0
digit8=0
digit9=0
digit10=0
digit11=0
digit12=0
digit13=0
digit14=0
digit15=0
digit16=0

if (countDigits == 13):
    digit1  =   (((n % 100) // 10) * 2)
    digit2  =   (((n % 10000) // 1000) * 2)
    digit3  =   (((n % 1000000) // 100000) * 2)
    digit4  =   (((n % 100000000) // 10000000) * 2)
    digit5  =   (((n % 10000000000) // 1000000000) * 2)
    digit6  =   (((n % 1000000000000) // 100000000000) * 2)
    digit7  =   (((n % 100000000000000) // 10000000000000) * 2)
    digit8  =   (((n % 10000000000000000) // 1000000000000000) * 2)
    digit9  =   (n % 10)
    digit10 =   ((n % 1000) // 100)
    digit11 =   ((n % 100000) // 10000)
    digit12 =   ((n % 10000000) // 1000000)
    digit13 =   ((n % 1000000000) // 100000000)
    check1  =   ((digit1 % 10) + (digit1 // 10))
    check1  =   check1 + (digit2 % 10) + (digit2 // 10)
    check1  =   check1 + (digit3 % 10) + (digit3 // 10)
    check1  =   check1 + (digit4 % 10) + (digit4 // 10)
    check1  =   check1 + (digit5 % 10) + (digit5 // 10)
    check1  =   check1 + (digit6 % 10) + (digit6 // 10)
    check1  =   check1 + (digit7 % 10) + (digit7 // 10)
    check1  =   check1 + (digit8 % 10) + (digit8 // 10)
    check1  =   check1 + (digit9 % 10) + (digit9 // 10)
    check1  =   check1 + (digit10 % 10) + (digit10 // 10)
    check1  =   check1 + (digit11 % 10) + (digit11 // 10)
    check1  =   check1 + (digit12 % 10) + (digit12 // 10)
    check1  =   check1 + (digit13 % 10) + (digit13 // 10)
elif (countDigits == 15):
    digit1  =   (((n % 100) // 10) * 2)
    digit2  =   (((n % 10000) // 1000) * 2)
    digit3  =   (((n % 1000000) // 100000) * 2)
    digit4  =   (((n % 100000000) // 10000000) * 2)
    digit5  =   (((n % 10000000000) // 1000000000) * 2)
    digit6  =   (((n % 1000000000000) // 100000000000) * 2)
    digit7  =   (((n % 100000000000000) // 10000000000000) * 2)
    digit8  =   (((n % 10000000000000000) // 1000000000000000) * 2)
    digit9  =   (n % 10)
    digit10 =   ((n % 1000) // 100)
    digit11 =   ((n % 100000) // 10000)
    digit12 =   ((n % 10000000) // 1000000)
    digit13 =   ((n % 1000000000) // 100000000)
    digit14 =   ((n % 100000000000) // 10000000000)
    digit15 =   ((n % 10000000000000) // 1000000000000)
    check1  =   ((digit1 % 10) + (digit1 // 10))
    check1  =   check1 + (digit2 % 10) + (digit2 // 10)
    check1  =   check1 + (digit3 % 10) + (digit3 // 10)
    check1  =   check1 + (digit4 % 10) + (digit4 // 10)
    check1  =   check1 + (digit5 % 10) + (digit5 // 10)
    check1  =   check1 + (digit6 % 10) + (digit6 // 10)
    check1  =   check1 + (digit7 % 10) + (digit7 // 10)
    check1  =   check1 + (digit8 % 10) + (digit8 // 10)
    check1  =   check1 + (digit9 % 10) + (digit9 // 10)
    check1  =   check1 + (digit10 % 10) + (digit10 // 10)
    check1  =   check1 + (digit11 % 10) + (digit11 // 10)
    check1  =   check1 + (digit12 % 10) + (digit12 // 10)
    check1  =   check1 + (digit13 % 10) + (digit13 // 10)
    check1  =   check1 + (digit14 % 10) + (digit14 // 10)
    check1  =   check1 + (digit15 % 10) + (digit15 // 10)
elif (countDigits == 16):
    digit1  =   (((n % 100) // 10) * 2)
    digit2  =   (((n % 10000) // 1000) * 2)
    digit3  =   (((n % 1000000) // 100000) * 2)
    digit4  =   (((n % 100000000) // 10000000) * 2)
    digit5  =   (((n % 10000000000) // 1000000000) * 2)
    digit6  =   (((n % 1000000000000) // 100000000000) * 2)
    digit7  =   (((n % 100000000000000) // 10000000000000) * 2)
    digit8  =   (((n % 10000000000000000) // 1000000000000000) * 2)
    digit9  =   (n % 10)
    digit10 =   ((n % 1000) // 100)
    digit11 =   ((n % 100000) // 10000)
    digit12 =   ((n % 10000000) // 1000000)
    digit13 =   ((n % 1000000000) // 100000000)
    digit14 =   ((n % 100000000000) // 10000000000)
    digit15 =   ((n % 10000000000000) // 1000000000000)
    digit16 =   ((n % 1000000000000000) // 100000000000000)
    check1  =   ((digit1 % 10) + (digit1 // 10))
    check1  =   check1 + (digit2 % 10) + (digit2 // 10)
    check1  =   check1 + (digit3 % 10) + (digit3 // 10)
    check1  =   check1 + (digit4 % 10) + (digit4 // 10)
    check1  =   check1 + (digit5 % 10) + (digit5 // 10)
    check1  =   check1 + (digit6 % 10) + (digit6 // 10)
    check1  =   check1 + (digit7 % 10) + (digit7 // 10)
    check1  =   check1 + (digit8 % 10) + (digit8 // 10)
    check1  =   check1 + (digit9 % 10) + (digit9 // 10)
    check1  =   check1 + (digit10 % 10) + (digit10 // 10)
    check1  =   check1 + (digit11 % 10) + (digit11 // 10)
    check1  =   check1 + (digit12 % 10) + (digit12 // 10)
    check1  =   check1 + (digit13 % 10) + (digit13 // 10)
    check1  =   check1 + (digit14 % 10) + (digit14 // 10)
    check1  =   check1 + (digit15 % 10) + (digit15 // 10)
    check1  =   check1 + (digit16 % 10) + (digit16 // 10)
mastercard = (n // 100000000000000)
amex = (n // 10000000000000)
visa = (n // 1000000000000000)
if (countDigits == 13):
    print("VISA\n")
elif (visa == 4):
    print("VISA\n")
elif (mastercard == 51 or mastercard == 52 or mastercard == 53 or mastercard == 54 or mastercard == 55):
    print("MASTERCARD\n")
elif (amex == 34 or amex == 37):
    print("AMEX\n")
else:
    print("INVALID\n")