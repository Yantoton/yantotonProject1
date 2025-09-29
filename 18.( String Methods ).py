a = "apple !!!!!!! apple???? apple @@@@ apple"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("?"))
print(a.replace("apple","yan"))
print(a.split(" "))
blogHeadling = "introduction tO Js"
print(blogHeadling.capitalize())

str1 = "welcome to the show????????"
print(len(str1.center(50)))
print(a.count("apple"))
print(str1.endswith("???????"))

str2 = "Mahiyan is a farmer . He is my friend"
print(str2.find("ishh"))
print(str2.index("is"))

str3 = "WelcomeToProgram"
print(str3.isalnum())

str4 = "Welcome90"
print(str4.isalpha())

str5 = "hi everyone"
print(str5.islower())

str6 = "happy birth day\n"
print(str6.isprintable())

str7 = "                 " # using Spacebar
print(str7.isspace())

str8 = "    " # using Tab
print(str8.isspace())

str9 = "Good Health Organzation"
print(str9.istitle())

str10 = "python is a interpreted language"
print(str10.startswith("python"))
print(str10.swapcase())

str11 = "His name is Tomal.Tomal love eating pizza"
print(str11.title())
