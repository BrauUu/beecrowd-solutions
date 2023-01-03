a, b = input().split()
c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

print(
    f'A = {a:.6f}, B = {b:.6f}\n'
    f'C = {c:.6f}, D = {d:.6f}'
)

print(
    f'A = {a:.1f}, B = {b:.1f}\n'
    f'C = {c:.1f}, D = {d:.1f}'
)

print(
    f'A = {a:.2f}, B = {b:.2f}\n',
    f'C = {c:.2f}, D = {d:.2f}',
    sep=''
)

print(
    f'A = {a:.3f}, B = {b:.3f}\n',
    f'C = {c:.3f}, D = {d:.3f}',
    sep=''
)

print(
    f'A = {a:.3E}, B = {b:.3E}\n',
    f'C = {c:.3E}, D = {d:.3E}',
    sep=''
)

print(
    f'A = {a:.0f}, B = {b:.0f}\n',
    f'C = {c:.0f}, D = {d:.0f}',
    sep=''
)
