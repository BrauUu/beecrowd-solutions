n, g = input().split()

runesArr = {}

for i in range(int(n)):
    ri, vi = input().split()
    runesArr[ri] = int(vi)
    
x = int(input())

recitedRunesArr = input().split()

sum = 0

for recitedRune in recitedRunesArr:
    sum += runesArr[recitedRune]
    
print(sum)
print("You shall pass!" if sum >= int(g) else "My precioooous")
