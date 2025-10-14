user = input("Hy enter a value number witch between 1 or 10(or 'start'or'quit' to exit):")
if user == "quit":
    print("Quitting the program")
elif user == "start":
    print("Starting the program")
else:
    try:
        num = int(user)
        if num > 10 or num < 1:
            raise ValueError(f"{user} is not between 1 and 10")
        else:
            print(f"{user} Is an integer between 1 and 10 is:",num)
    except Exception as e:
        print("invalid input",e)
