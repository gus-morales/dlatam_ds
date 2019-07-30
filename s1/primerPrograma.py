for i in range(3):
    print("str_%s"%i)

num = 20

print(num)

str_var1 = "intro a python"
str_var2 = "bla"

print(num+num)

print(str(num)+str_var1)

print(len(str_var2)+num)

name = "Gustavo"
lname = "Morales"

print("My name is " + name + " " + lname)
print("My name is {} {}".format(name,lname))
print("My name is %s %s"%(name,lname))
print(name.count("a"))
print(lname.upper())