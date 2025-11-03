f = open('ythello1file.txt','r')
g = 0
while True:
    g = g + 1
    line = f.readline()
    if not line :
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f'the shed {g} cow tag number is:{m1}')
    print(f'the shed {g} calf tag number is:{m2}')
    print(f'the shed {g} bull tag number is:{m3}')
    print(line)
