def main():
    ch = input("Enter the change: ")
    while True:
        if type(ch) == int or type(ch) == float:
            if float(ch) > 0:
                break
            else:
                ch = input("Invalid input. Enter again: ")
        else:
            ch = input("Invalid input. Enter again: ")


    ich = round(float(ch) * 100)
    quarters = ich // 25
    dimes = (ich % 25) // 10
    nickels = ((ich % 25) % 10) // 5
    pennies = ((ich % 25) % 10) % 5
    total = quarters + dimes + nickels + pennies
    print(total)
main()