n, c, m = input().split()


stampedStickers = input().split()
boughtStickers = input().split()
alreadyFoundStickers = []

count = 0
    
for i in range(len(stampedStickers)):
    for g in range(int(m)):
        if boughtStickers[g] == stampedStickers[i]:
            try:
                if alreadyFoundStickers.index(boughtStickers[g]):
                    continue
            except:
                alreadyFoundStickers.append(boughtStickers[g])
                count += 1
        
print(int(c) - count)
    