def calculaetGmean(a,b):
    mean = (a+b)
    print(mean)
a = 10
b = 20

calculaetGmean(a,b)

from datetime import datetime

def get_time() -> str:
    now: datetime = datetime.now()
    return now. strftime('%H:%M:%S')

print(get_time())

def connent():
    raise NotImplementedError("connect() is missing code")


connent()

def average(a=86,b=20):
    print("The average is",(a+b)/1)

average(86,20)


def name(fname,mname = "Rabby",lname = "Hossien"):
    print("Hy,",fname,mname,lname)

name("Rahat","Islam","Shovon")

def car_list():
    cars: dict[int, str] = {1:'Gt86', 2:'Mitsubishi', 3:'Subaru', 4:'Rx7', 5:'Supra mk4'}
    return cars

print(car_list())


def average(*numbers):
    print(type(numbers))
    sum = 0
    for n in numbers:
        sum = sum + n
        print("Average is:",sum / len(numbers))

average(1,2,3,4,5,6)

def name(**name):
    print(type(name))
    print("Hy,", name["fname"], name["mname"], name["lname"])

name(mname="Islam", lname="Tisha", fname="Toha")

def call_yan():
    print("Hy yan!")
    print("what program you learning is it python?")
    print("yan says : yes i am learning python programming")

call_yan()

def calc_rect_area(width, height, lenght):
    area = width * height * lenght
    print("The total area is", area)

calc_rect_area(12,15,28)
