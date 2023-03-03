n = int(input())

for i in range(n):
    x = input()
    
    countOfLikeOne = 0
    countOfLikeTwo = 0
    countOfLikeThree = 0
    
    for g in range(len(x)):
        if (x[g] == 'o' and g == 0) or (x[g] == 'n' and g == 1) or (x[g] == 'e' and g == 2):
            countOfLikeOne += 1
        if (x[g] == 't' and g == 0) or (x[g] == 'w' and g == 1) or (x[g] == 'o' and g == 2):
            countOfLikeTwo += 1
        if (x[g] == 't' and g == 0) or (x[g] == 'h' and g == 1) or (x[g] == 'r' and g == 2) or (x[g] == 'e' and (g == 3 or g == 4)):
            countOfLikeThree += 1
    
    if countOfLikeOne >= countOfLikeThree and countOfLikeOne > countOfLikeTwo and len(x) == 3:
        print(1)
    elif countOfLikeTwo >= countOfLikeThree and countOfLikeTwo > countOfLikeOne and len(x) == 3:
        print(2)
    elif countOfLikeThree >= countOfLikeOne and countOfLikeThree >= countOfLikeTwo and len(x) == 5:
        print(3)
