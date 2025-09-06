bd_city1 = {"Dhaka",'Chittagong','Comilla','Thakurgaon'}
bd_city2 = {"Sylhet",'Rajshahi','Rangpur','Khulna','Comilla'}
print(bd_city1.issuperset(bd_city2))
bd_city3 = {"Dhaka",'Thakurgaon','Chittagong'}
print(bd_city1.issuperset(bd_city3))
print(bd_city3.issubset(bd_city1))
print(bd_city3.isdisjoint(bd_city2))
