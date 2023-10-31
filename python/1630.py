def euclides(bigger, smaller):
    if smaller == 0:
        return bigger
    else:
        return euclides(smaller, bigger % smaller)
        
res = ''

while True:
    try:
        x, y = list(map(int, input().split()))
        num = 0
        
        bigger = x if x > y else y
        smaller = y if x > y else x
        print(int((x * 2 + y * 2) / euclides(bigger, smaller)))
       
    except:
        break