n = int(input())

for i in range(n):
    c = input()
    
    resp = ''
    
    for char in c:
        if char.islower():
            resp = char + resp
            
    print(resp)