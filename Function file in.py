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

def car_list():
    cars: dict[int, str] = {1:'Gt86', 2:'Mitsubishi', 3:'Subaru', 4:'Rx7', 5:'Supra mk4'}
    return cars

print(car_list())
