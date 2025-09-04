a = 0
b = 1
count = 0
fib = 0
sum = 0

num = int(input("Enter a number: "))

for count in range(0,num):
 if count <= 1:
   fib = count
   print(fib)

 else:

    fib = a + b
    a = b
    b = fib
    print(fib)
    sum = sum + fib
    count = count + 1

print(sum)
