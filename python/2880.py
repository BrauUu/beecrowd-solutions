x = input()
w = input()
count = 0

for i in range(len(x) - len(w) + 1):
    flag = False
    j = 0
    for g in range(i, i + len(w)):
        if x[g] == w[j]:
            flag = True
            break
        j += 1
    if flag:
        continue
    else:
        count += 1

print(count)