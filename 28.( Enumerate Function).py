marks = [12,45,86,35,12,1,0,4]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 2):
#         print("toton, pass ")
#     index += 1

for index,mark in enumerate(marks):
    print(mark)
    if (index == 2):
        print(f"toton your mark is {mark}  pass ")
    elif (index == 6):
        print(f"semon your mark is {mark}  fail")
    index += 1
