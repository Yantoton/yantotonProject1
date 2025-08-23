this_tuple = ("Farm", "Car", "Code")
print(this_tuple)

#Items[0]:
this_tuple = ("Farm", "Car", "Code")
print(this_tuple[0])

#Allow Duplicates:
this_tuple = ("Farm", "Car", "Code", "Farm", "Car", "Code")
print(this_tuple)

#Length - len():
this_tuple = ("Farm", "Car", "Code")
print(len(this_tuple))

#Create Tuple With One Item:
my_tuple = ("Think Big",)
print(type(my_tuple))
#Not a Tuple
my_tuple = ("Think Big")
print(type(my_tuple))

#Tuple Items - Data Types

tuple1 = ("Farm" "Car" "Code")
tuple2 = (246108)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)
print(type(tuple1),tuple1)
print(type(tuple2),tuple2)

#The tuple() Constructor
my_tuple1 = tuple (("Farm" ,"Car" ,"Code"))
print(my_tuple1)


countries = ("Bangladesh","Italy","Lasvegas","India","England","Germany")
tap = list(countries)
tap.remove("India")
tap.append("China")
tap.pop(2)
tap[3] = "Japan"
countries = tuple(tap)
print(countries)

countries = ("Pakistan","katar","Afghanistan","Shilanka",)
countries2 = ("Thailand","Vietnam","Korea","Singapore")
southEastAsia = countries + countries2
print(southEastAsia)









