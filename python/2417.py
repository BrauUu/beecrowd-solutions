cv, ce, cs, fv, fe, fs = list(map(int, input().split()))

cp = cv * 3 + ce
fp = fv * 3 + fe

if cp > fp:
    print('C')
elif fp > cp:
    print('F')
else:
    if cs > fs:
        print('C')
    elif fs > cs:
        print('F')
    else:
        print('=')