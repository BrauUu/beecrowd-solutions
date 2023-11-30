n = int(input())

order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(n):
    m = int(input())
    x = list(input())
    swap = 0
    error = False
    for j in range(m):
        if swap <= 1:
            if x[j] != order[j]:
                ind = order.index(x[j])
                if order[j] == x[ind]:
                    temp = x[j]
                    x[j] = order[j]
                    x[ind] = temp
                    swap += 1
                else:
                    swap += 2
        else:
            error = True
            break
        
    print('There are the chance.' if error == False else "There aren't the chance.")
        
                