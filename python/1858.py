x = int(input())
lower = 21
res = 0

people = input().split()

for i in range(len(people)):
    if int(people[i]) < lower:
        lower = int(people[i])
        res = i+1
        
print(res)
    