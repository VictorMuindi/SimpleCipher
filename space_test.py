import re

def remove(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)

message = "defend the walls"

print(remove(message))