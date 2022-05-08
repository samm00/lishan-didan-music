import re

f = open("f.txt", "r")
s = f.read()

s = re.sub(r'\n', '\n<br>', s)

print(s)

