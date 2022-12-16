x = input()
y = input()
z = input()

print(
    f'{x}{y}{z}\n'
    f'{y}{z}{x}\n'
    f'{z}{x}{y}\n'
    f'{x[:10]}{y[:10]}{z[:10]}'
)
