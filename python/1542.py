while True:
    try:
        q, d, p = list(map(int, input().split()))
        
        res = int((d * q / (p-q)) * p)
        
        print(f'{res} paginas' if res > 1 else f'{res} pagina')
        
    except:
        break