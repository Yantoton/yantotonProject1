#Append 
sport_list = ['Soccer','Cricket','Basketball',"Football"]
sport_list.append('Ufc')
print(sport_list)

#Clear
sport_list = ['Soccer','Cricket','Basketball',"Football"]
sport_list.clear()
print(sport_list)

#Copy
sport = ['Soccer','Cricket','Basketball',"Football"]
copy_sport: list[str] = sport.copy()

copy_sport.remove(sport[0])
print(sport)
print(copy_sport)

#Count
sport = ['Soccer','Cricket','Basketball',"Football",'Football']
football = sport.count('Football')

print(football)

#Extend
sport = ['Soccer','Cricket','Basketball','Football']
sport2 = ['Apple','Banana']

sport.extend(sport2)
print(sport)

#Insert
sport = ['Soccer','Cricket','Basketball','Football']
sport.insert(5,'Kabadi')
print(sport)

sport = ['Soccer','Cricket','Basketball','Football']
popped = sport.pop(2)
print(popped)
print(sport)

#Remove
sport = ['Soccer','Cricket','Basketball','Football']
sport.remove('Cricket')
print(sport)

#Reverse
sport = ['Soccer','Cricket','Basketball','Football']
sport.remove('Cricket')
print(sport)

#Sort
sport = ['Soccer','Cricket','Basketball','Football']

sport.sort(key=lambda sport: len(sport), reverse=True)

print(sport)

