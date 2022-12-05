n = int(input())

n1 = int(input())

count = 0

participants = []

for i in range(n):
    participants.append(int(input()))
    
participants.sort(reverse=True)

i = 0
while True:
    if count >= n1: break
    g = i
    try:
        while participants[g] == participants[i]:
            count += 1
            g += 1
        i = g
    except:
        continue

print(count)