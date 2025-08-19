farm_list = ["Milking cow -100","Fattening Bull-200","Calf -100","Dog -40","Goat -20","Parot Birds -500","Sheep -25","fish_1000"]
for farm in farm_list:
    print(farm)
print(farm_list)

t = [11,21,4,5,15,16,1,16,76,79,64]

m = [86000,2456,786210]

c = [12786,9746564,47465,468643]

y = t+m+c
print(y)
for t,m,c in zip(t,m,c):
    print(t,m,c)
