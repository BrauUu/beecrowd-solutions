entry = input()
temp = ''
for char in entry:
    if char == "7":
        temp += '0'
    else:
        temp += char
    
n1, operator, n2 = temp.split()

if operator == 'x':
    operator = '*'

res = str(eval(f"{int(n1)} {operator} {int(n2)}"))
otherTemp = ''
for char in res:
    if char == "7":
        otherTemp += "0"
    else:
        otherTemp += char

print(int(otherTemp))