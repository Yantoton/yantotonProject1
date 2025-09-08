dic = {
12:"yan",
123:"Toton",
34:"Mahu",
345:"Mahiyan"
}
print(dic[345])

info = {'name':'Haseb','age':22,'Student':True}
print(info['name'])
print(info['age'])
print(info['Student'])
print(info.keys())
print(info.items())
for key,vs in info.items():
    print(f"The value of info key {key} is: {info[key]}")
    if key in info:
        print(" Bro info is Right")
