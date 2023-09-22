l = input()
x = input()

res = ''

for letter in x:
    y = ord(letter) - 97
    res += l[y]
    
print(res)