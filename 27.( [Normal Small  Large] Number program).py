num = int(input("Enter a large number: "))
if num <0 or num < 50:
    print(f"{num} is  small number")
elif num < 50 or num >=100:
    print(f"{num} is large number")
else:
    print(f"{num} is normal number")
