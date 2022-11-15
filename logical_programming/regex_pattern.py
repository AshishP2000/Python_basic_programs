import re

number = "91 9156524636"
x = re.search("[91]\s[0-9]{10}",number)

if x:
    print("Pattern matches")
else:
    print("Pattern did not match")