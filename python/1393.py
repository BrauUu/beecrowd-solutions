i = 0
fibL = [1,1]
while i <= 40:
    j = i + 2
    fibL.append(fibL[j-2] + fibL[j-1])
    i += 1
    
while True:
    n = int(input())
    
    if n == 0:
        break
    
    print(fibL[n])