import re

regex = "^((n|N)ormal)|((o|O)verweight)|((o|O)besity)|((u|U)nderweight)$"
value = "No"
value2 = "normal"

a = re.match(regex, value)
print(a)
print(re.match(regex, value))

if a:
    print(a.re + "   ADSSADA")
elif a is None:
    print("FALSE")
    print(a)
else:
    print("jk lol")