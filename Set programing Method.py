# All Set Programin Method For Python

car1 = {'Gt86','Subaru','Mitsubishi'}
car2 = {"Rx7","Supra mk4","BMW"}
car1.add("premio")
car1.remove("premio")
car1.clear()
car1.update(car2)
my_garrage = car1.union(car2)
print(car1.difference(car2))
print(car2.intersection(car1))

for x in my_garrage:

    print(x)

    if 'Gt86' in x:
        print("Yes 1day you will buy your dream car Gt86")
