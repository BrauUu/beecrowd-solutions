while True:
    try:
        a, b, c = list(map(int, input().split()))
        
        if a == b == c:
            print('*')
        elif c == b and a != c:
            print('A')
        elif a == c and b != a:
            print('B')
        elif a == b and c != a:
            print('C') 
    except:
        break