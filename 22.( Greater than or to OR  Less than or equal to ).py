num = 13
if num < 0:
    print("num is negative")
elif num > 0:
    if num <= 10:
        print("num is between 1 and 10")
    elif num > 10 and num <= 20:
        print("num is between 11 and 20")
    else:
        print("num is greater than 20")

else:
    print("num is zero")
