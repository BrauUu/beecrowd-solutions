n = int(input())

searchs = []

for i in range(n):
    searchs.append(input())
    
q = int(input())

for i in range(q):
    actualSearch = input()
    count = 0
    largerSearch = 0
    
    for search in searchs:
        if search.find(actualSearch) == 0:
            count += 1
            if len(search) > largerSearch:
                largerSearch = len(search)
    
    if count == 0:
        print(-1)
    else:
        print(f'{count} {largerSearch}')