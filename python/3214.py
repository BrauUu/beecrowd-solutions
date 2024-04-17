e, f, c = list(map(int, input().split()))

emptyTotal = e + f
sodaDrinked = 0
while emptyTotal >= c:
    temp = emptyTotal // c
    sodaDrinked += temp
    emptyTotal = emptyTotal % c
    emptyTotal += temp
print(sodaDrinked)