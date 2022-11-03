n = int(input())

for i in range(n):
    x = input().split()
    hour = x[0]
    minutes = x[1]
    isOpened = int(x[2])
    
    option = ''
    
    if isOpened == 1:
        option = 'abriu'
    elif isOpened == 0:
        option = 'fechou'
        
    print(f'{hour:0>2}:{minutes:0>2} - A porta {option}!')