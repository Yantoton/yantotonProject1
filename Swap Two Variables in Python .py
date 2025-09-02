# Solution-1(Using Third Variable)
f = 43
j = 21

shift = f
print("The value of shift variable is", shift)
f = j
print("The value of j variable is", j)
f = shift
print("The value of f variable is", f)

# Solution-2(WithOut Using Thrid Variable)
o = 5
c = 6
o, c = c, o
print("The value of c variable is", c)
print("The value of o variable is", o)
