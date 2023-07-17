n = int(input())
input()
for i in range(n):
    treesSpecies = {}
    count = 0
    while True:
        try:
            treeSpecie = input()
            if treeSpecie == '':
                break                            
            
            treesSpecies.update({treeSpecie : treesSpecies.get(treeSpecie, 0) + 1})
            count += 1
            
        except:
            break
        
    orderList = sorted(treesSpecies, key=lambda x: x)
    
    if i >= 1:
        print()
        
    for item in orderList:
        print(f'{item} {(int(treesSpecies.get(item, 1)) / count * 100):.4f}')