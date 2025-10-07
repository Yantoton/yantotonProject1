def multiply (a):
    for i in range(1,11):
        print(a,"x",i,"=",a * i)

        if i == 11:
            break
        else:
            continue

a=int(input("enter a number: "))
print("Multiplication is done!!!... ")

multiply(a)
