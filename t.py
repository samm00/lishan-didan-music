import re

f = open("f.txt", "r")
s = f.read()

s = re.sub(r'\d:\d\d\n', '<br>', s)

print(s)

