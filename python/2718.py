n = int(input())

for i in range(n):
    dec = int(input())
    binary = bin(dec)
    
    count = 0
    gt = 0
    
    for g in range(2, len(binary), 1):
        if binary[g] == '1':
            count += 1
        else:
            if count > gt:
                gt = count
            count = 0
    if count > gt:
        gt = count
    
    print(gt)