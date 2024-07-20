while True:
    try:
        i,f,c,s = input().split(' ', maxsplit=3)
        print(f'{i}{f}{c}{s}')
        print(f'{i}        {float(f):.6f}        {c}        {s}')
        print(f'{" " * ((10 - len(i)) if len(i) < 10 else 0)}{i}{" " * ((10 - len(f)) if len(f) < 10 else 0)}{f}{" " * 9}{c}{" " * ((10 - len(s)) if len(s) < 10 else 0)}{s}')
    except EOFError:
        break