PI = 3.1415926535897

while True:
    try:
        a, b, c = list(map(int, input().split()))

        p = (a+b+c)/2
        At = (p*(p-a)*(p-b)*(p-c))**(1/2)

        r = At / ((a/2)+(b/2)+(c/2))
        Ac = (r)**2 * PI

        Abc = ((a*b*c)/(4*At))**2 * PI
        Abc -= At
        At -= Ac

        print(f'{Abc:.4f} {At:.4f} {Ac:.4f}')
    except EOFError:
        break