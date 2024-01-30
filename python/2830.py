def fn(b,s):
    x = (b + 1) // 2
    if s < 2 * x and s > 2 * (x-1):
        print('oitavas')
        return
    x = (b + 3) // 4
    if s < 4 * x and s > 4 * (x-1):
        print('quartas')
        return
    x = (b+7) // 8
    if s < 8 * x and s > 8 * (x-1):
        print('semifinal')
        return
    else:
        print('final')

k = int(input())
l = int(input())

b, s = (k, l) if k > l else( l, k)
fn(b,s)