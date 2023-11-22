n = int(input())
piecesCount = 1

while n >= 2:
    piecesCount *= 4
    n /= 2
    
print(piecesCount)