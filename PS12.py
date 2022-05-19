fname = input("Enter first name")
lname = input("Enter last name")
print(fname, lname)

name = fname.replace("aniel", ".")
nlname = lname.replace("oa", "oa,")
print(nlname, name)

txt = input("Enter text")
txt2 = txt[::-1]
print(txt2)


ntext = input("Enter another text")
print(ntext)
print(*ntext, sep = "\n")



ntext2 = input("Enter another text")
Cha = input("How many characters do you want to print")
lines = input("How many lines do you want printed?")
dir = input("What direction do you want the shift?")
print(ntext2)
r_rot = 1
l_rot = 2
shift = (ntext2 * 3)[len(ntext2) + r_rot - l_rot : 2 * len(ntext2) + r_rot - l_rot]
print(str(shift))

r_rot = 1
l_rot = 2
shift2 = (str(shift) * 3)[len(str(shift)) + r_rot - l_rot : 2 * len(str(shift)) + r_rot - l_rot]
print(str(shift2))


