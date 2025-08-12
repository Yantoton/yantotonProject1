numbers = list(range(0,100))
for number in numbers:
    if number > 50:
        break
    print(number ,end=" ")

while True:
    name = input("what is user name(w to continue,s to quit)")
    if name == "s":
        break
    elif name == "w":
        continue
    print("welcome in loop ",name)

num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
         continue
    print("even num",num,end=" ")
