n = int(input())

for i in range(n):
    shoppingList = input().split()
    newShoppingList = []
    for item in shoppingList:
        if newShoppingList.count(item) == 0:
            newShoppingList.append(item)
    
    print(" ".join(sorted(newShoppingList)))