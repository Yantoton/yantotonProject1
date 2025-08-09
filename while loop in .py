count = 10
while(count > 0):
  print(count)
  count = count -1

count = 10
while(count > 0):
  print(count)
  count = count +1

y = 0
while (y < 10):
  print(y)

y = 0
while (y < 10):
  print(y)
y = y +1

t = int(input("Enter your number:))
while (y < 36):
   t = int(input("Enter your number:))
   print(y)
  y = y +1

name = input("What is your name?")
while name == "":
    print("please enter your name")
else:
    print(f"Hello {name}")



name = input("What is your name?")

while name == "":
    print("please enter your name")
    name = input("What is your name?")
print(f"Hello {name}")



age = int(input("What is your age?"))

while age < 0 :
    print("age can't be negative")
    age = int(input(" What is your age?"))
print(f"your age is {age}")


while not food == "q":
    print(f"Your favorite food is {food}")
    food = input("What is your another favorite food? (q to quit)")
print("just bye")

num = int(input("Enter a # between 1 - 10:"))


while num < 1 or num > 10:
    print(f"{num} is invalid")
    num = int(input("Enter a # between 1 - 10:"))

print(f"{num} is valid")


number = 1
while number <= 10:
    print(number)
    if number % 2 != 0:
        print(number, end=" ")
        number += 2
      
        print("is even")

    else:
        print("is odd")

product = 1
number = 1
while number <= 5:
    product = product * number
    number = number + 1
    print(product)
  

sentence = input("Enter a sentence = ")
words = sentence.split()
for word in words:
    i = len(word) -1
    while i >= 0:
        print(word[i], end=" ")
        i -= 1
        print(end=" ")
      

  word = input("Enter a word to check:")
vowels = "aeiou"
count = 0
index = 0

while index < len(word):
    if word[index].lower () not in vowels and word[index].isalpha():
        count += 1
    index += 1

print(f"Number of consinants:", count)

