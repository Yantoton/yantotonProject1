 simple calculator program
 __________________________
 operator = ("enter the operator(+,-,*,/)")
 a = int(input("Enter the first number"))
 b = int(input("Enter the second number"))

 print("The value of number",a,"+",b,"=",a+b)
 print("The value of number",a,"-",b,"=",a-b)
 print("The value of number",a,"*",b,"=",a*b)
 print("The value of number",a,"/",b,"=",a/b)
 print("The value of number",a,"%",b,"=",a%b)
 print("The value of number",a,"//",b,"=",a//b)
 print("The value of number",a,"**",b,"=",a**b)

 data type program in python
 ____________________________

 print("Dancer omur")

 a = "2"
 b = "3"
 print(int(a) + int(b))

 a = 8
 print(type(a))
 b = 6.6
 print(type(b))
 c = a+b
 print(type(c))
 print(c)

 user input program in python
 _____________________________
 a = input("Enter user password input:")
 print("hi\nwelcome:" , a)


 operator = input("Enter the operator(+,-,*,/):")
 b = float(input("Enter the 1st number:"))
 c = float(input("Enter the 2nd number:"))

 if operator == "+":
     result = b + c
     print(round(result,3))

 elif operator == "-":
     result = b - c
     print(round(result,3))

 elif operator == "*":
     result = b * c
     print(round(result,3))

 elif operator == "/":
     result = b / c
     print(round(result,3))

 else:
     print("Operator not supported")


 d = input("Enter your name:")
 print("welcome", d)

 x = input("Enter your first input:")
 y = input("Enter your second input:")
 print(x + y)

 print("The value of 'x' is ",x,".")
 print("The value of 'y' is ",y,".")

 string in python
 ________________

 name = "Yan"
 friend = "Mahiyan"
 anotherFriend = "Toton"
 gt86 = '''Yan said
 hi Friends
 all good
 one day i will buy my dream car
 toyota gt86 In-sha-Allah'''

 print("Hello," + name)
 print("Friend")
 print("anotherFriend")
 print("gt86,"+gt86)
 print(friend[0])
 print(friend[1])
 print(friend[2])
 print(friend[3])
 print(friend[4])
 print(friend[5])
 print(friend[6])

 print("Lets use a for loop\n")
 for cheracter in gt86:
     print("character",cheracter)

 every f-string trick in python
 ________________________________
 name: str = 'Indently'
 age: int = 21
 print('name:' + 'Indently,','age:' + str(age))
 print(f'name:{name} age:{age}).1 + 1 = {1 + 1},quick maths.')

 var: int = 100
 print(f'{var=}')
 print(f'{isinstance(var,int)=}')
 print(f'{1 + 1 = }')

 decimal: float = 86.18
 precent: float = .1012

 print(f'{decimal:.2f}')
 print(f'{precent:.2%}')

  big_num:int = 1522025862026
 print(f'{big_num:,}')

 from datetime import datetime
 now:datetime = datetime.now()
 print(f'{now:%x}')
 print(f'{now:%c}')
 print(f'{now:%H:%M:%S}')

 user: str = 'Indently'
 path: str = fr'\user\{user}\Documents'
 print(f'{path}')
 print(f'{1 + 1} {f'{2 + 2} {f'{3 + 3} {f'{4 + 4}'}'}'}')

 text:str = 'Yan_toton'
 print(f'{text:.>{15}}')
 print(f'{text:.^{86}}')
 print(f'{text:.<{20}}: Hi Mahiyan')





















 car = "toyota gt86"
 len1 = len(car)
 print("gt86 is a",len1,"letters")

 farm = "cow,bull,dog,fish,chicken,many more"
 len2 = len(farm)
 print("cow,bull,dog,fish,chicken,many more is a",len2,"letters word")
 print(farm[:])

 practice
 age: int = 29
 name: str = 'toton'
 print('Name:'+ name +',Age:'+ str(age))
 print(f'name:{name},Age:{age}')

 def add(a: float, b: float) -> float:
     print(f'Adding {a} + {b} = {a+b}')
     return a+b
 print(add(10,20))
 print(add(8531,48641))

 def func()-> None:
     print('yes')

 func()
 func()
 func()
 func()
 func()
 func()

 for i in range(6):
     print('yoho')

 dream: list[str] = ['Farming','buy Gt86','Coding,']

 for dream in dream:
     print(f'my_dream, {dream}')
     print('....')

 y: int = 0
 while y < 2:
     print(y)
     y += 1

 a: int = 1
 b: int = 2

 print(a > b)
 print(a < b)
 print(a == b)
 print(a != b)
 print(a >= b)
 print(a <= b)

 from datetime import datetime
 now: datetime = datetime.now()
 print(f'now is: {now:%x}')
 print(f'now is: {now:%c}')
 print(f'now is: {now:%H,%M,%S})

String Methods in python

 a = "Yan toton !!!!! Yan toton"
 print(len(a))
 print(a)
 print(a.upper())
 print(a.lower())
 print(a.rstrip("!"))
 print(a.replace("Yan toton","Mahiyan"))
 print(a.split(" "))
 blogHeading = "introductinon tO jS"
 print(blogHeading.capitalize())

 str1 = "welcome to the code!!!"
 print(len(str1))
 print(len(str1.center(50)))
 print(a.count("!"))

 str1 = "welcome the game???"
  print(str1.endswith("???")

 str1 = "Welcome to the code!!!"
 print(str1.endswith("to",0,10))

 str1 = "he's name is rahul. he is an honest person."
 print(str1.find("ishh"))
 print(str1.find("ishh"))

 str1 = "Welcome to the code!!!"
 print(str1.isalnum())
 str1 = "Welcome"
 print(str1.isalpha())

 str1 = "hello mahiyan"
 print(str1.islower())

 str1 = "we wish you eid mubarak\n"
 print(str1.isprintable())
 str1 = "       " using spacebar
 print(str1.isspace())
 str2 = " " using tab
 print(str2.isspace())

 str1 = "Animal Health Organization"
 print(str1.istitle())

 str2 = "To kill a Mocking bird"
 print(str2.istitle())

 str1 = "Python is a Interpreted Language"
 print(str1.startswith("Python"))

 str1 = "his name is Karim.karim is a good man."
 print(str1.title())

 a = int(input("Enter your age:"))
 print("Your age is:",a)

 print(a>18)
 print(a<=18)
 print(a>=18)
 print(a==18)
 print(a!=18)
 if(a>18):
     print("You can drive")
 else:
     print("You cannot drive")

 num = int(input("Enter the value of num:"))
 if (num < 0):
     print("Number is negative.")
 elif (num == 0):
     print("Number is zero.")
 else:
     print("Number is positive.")

'''time if else program making python'''

 import time
 timestamp = time.strftime('%H:%M:%S:')
 print(timestamp)
 timestamp = str(time.strftime('%H:'))
 print(timestamp)
 timestamp = str(time.strftime('%M:'))
 print(timestamp)
 timestamp =str(time.strftime('%S:'))
 print(timestamp)

 if 6  <= str.isdigit(timestamp) <=12:
     print("Good morning Sir!")
 elif 12 <= str.isdigit(timestamp) <=18:
     print("Good afternoon Sir!")

 else:
     print("Good evening OR Good night Sir!")

 import time

 def connect() -> None:
     print('Connecting to server...?')
     time.sleep(4)
     print('You are connected!')

 connect()

 def want_to_smokeweed(name:str, age:int, has_id: bool) -> None:
     if name.lower() == 'Nowrin':
         print('Get out of here Nowrin, we don\'t want to smoke whit you')
         return
     if age >= 21 and has_id:
         print('You can smoke weed whit us!..')
     else:
         print('You can\'t smoke weed with us!...')

  def mani() -> None:
      smoke_weed('Nowrin',18,has_id=False)
      smoke_weed('kabib',21,has_id=False)
      smoke_weed('leon', 22, has_id=False)

 cars = ["Gt86","Mitsubishi","Subaru","RX7"]
 for car in cars:
     print(car)
     for i in cars:
         print(i)
         if (i == "Gt86"):
             print("this is my dream car")



 from datetime import datetime

 current_time = datetime.now()

 hour_integer = current_time.hour

 if 12<=hour_integer<13:
     print('Weak up & get fresh & take breakfast')
 elif 13<=hour_integer<15:
     print('study fc & keep practice')
 elif 15<=hour_integer<17:
     print('take care ruhu & give birds and dog food & Lunch')
 elif 17<=hour_integer<19:
     print('workout time & Snack')
 elif 19<=hour_integer<20:
     print('Return Home & do anykind of house work')
 elif 20<=hour_integer<23:
     print('Family&Friends time & Learnin new code & learn new thinks')
 elif 23<=hour_integer<24:
     print('Go to outside for walk or bike ride')
 elif 24<=hour_integer<1:
     print('Play Fortnite game & dinner & coco dinner')
 elif 1<=hour_integer<4:
     print('Again study fc & keep practice & complete task')
 elif 4<=hour_integer<5:
     print('Watch Farming video on youtube')
 else:
     print('Your bed is calling it\'s sleep time')

 cars = ["Gt86","Subaru","Mitsubishi","Rx7","Bmw "]
 for car in cars:
  print(car)
  for i in car:
         print(i)

 i = 100
 while i > 0:
     print(i)
     i = i -1
 else:
     print("else mood is on!")

 age = int(input("Enter your age:"))

 while age < 0:
     print("Your age cannot be negative")
     age = int(input("Enter your age"))

 print(f"Your are {age} years old")
































































