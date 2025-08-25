
name = input("Enter player name:")

print("Welcome to P.T.M Quize Game "+name)

q_list = ["Witch Cattle Breed is most Famuse for Fattening purpose"]
print(q_list)

op = ("Your Option are:", 'A.Sahiwal','B.RCC', 'C.Gir', 'D.North Bengal')
print(op)

answer = input("Enter the your Option:")

if answer in op:
    print("Correct Answer 'A.Sahiwal' is Most Famuse breed fo Fatteinng", )
else:
    print("Wrong Answer please give the correct answer")
