n = int(input())

for i in range(n):
    x, y = input().split()
    cont = 0
    temp = [item for item in x]
    for g in range(len(temp)):
        while True:
            if temp[g] != y[g]:
                cont += 1
                code = ord(temp[g])
                temp[g] = chr(code + 1 if code + 1 <= 122 else 97)
            else:
                break  
    
    print(cont)