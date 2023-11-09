n = int(input())

for _ in range(n):
    text = input().split()
    word = input()
    pos = []
    ind = 0
    
    for w in text:
        if w == word:
            pos.append(ind)
        ind += len(w) + 1
    
    if len(pos) == 0:
        pos.append(-1)
    
    print(*pos)