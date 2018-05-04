import re

regex2 = "^(((0[1-9])|([1-31]))|[1-2][0-9]|3(0|1))(/)(((0[1-9])|([1-12]))|1[0-2])(/)(19|20)[0-9]{2}$"
regex = "^(((0[1-9])|([1-31]))|[1-2][0-9]|3(0|1))(/)(((0[1-9])|([1-12]))|1[0-2])(/)$"
value = "1/1/1994"
valuec = "01/1/1994"
valued = "1/12/1994"
value2 = "13/12/1994"



a = re.match(regex2, value)
b = re.match(regex2, value2)
c = re.match(regex2, valuec)
d = re.match(regex2, valued)
print(a)
print(b)
print(c)
print(d)

# if a:
#     print(a.re + "   ADSSADA")
# elif a is None:
#     print("FALSE")
#     print(a)
# else:
#     print("jk lol")