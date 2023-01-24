while True:
    n = int(input())
    
    if n == 0:
        break
    
    x = ['A', 'B', 'C', 'D', 'E', 'F']
    
    for i in range(n):
        options = input().split()
        optionSelected = ''
        count = 0
        
        for j in range(5):
            if int(options[j]) <= 127:
                optionSelected = x[j]
                count += 1
                
        if count == 1:
            print(optionSelected)
        else:
            print('*')