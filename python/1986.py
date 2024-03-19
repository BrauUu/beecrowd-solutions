caracteres_hex = {}

for i in range(97, 123):  
    caracter = chr(i)
    hex_code = str(hex(i)).upper()[2:]
    caracteres_hex[hex_code] = caracter

n = int(input())

l = input().split()
res = ''

for el in l:
    res += caracteres_hex[el]

print(res)