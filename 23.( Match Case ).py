x = int(input("Enter a value of x:"))

match x:

    case 0:
        print("x is zero")
    case 10:
        print("x is 4")
    case _ if x!=100:
        print(x,"is not 100")
    case _ if x==80:
        print(x,"is 80")
    case _:
        print(x)

print("program end here!....")


def month_of_year(year):
    match year:
        case 1:
            print("It is January")
            return True
        case 2:
            print("It is February")
            return True
        case 3:
            print("It is March")
            return True
        case 4:
            print("It is April")
            return True
        case 5:
            print("It is May")
            return True
        case 6:
            print("It is June")
            return True
        case 7:
            print("It is July")
            return True
        case 8:
            print("It is August")
            return True
        case 9:
            print("It is September")
            return True
        case 10:
            print("It is October")
            return True
        case 11:
            print("It is November")
            return True
        case 12:
            print("It is December")
            return True
        case _ :
            print("Not a valid year")
            return False

print(month_of_year(7))
print('End here!...')
