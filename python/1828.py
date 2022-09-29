x = int(input())

results = {
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "tesoura": ["papel", "lagarto"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

for i in range(1, x + 1):
    
    bazinga = False
    
    y1, y2 = input().split()
    for g in results[y1]:
        if g == y2:
            bazinga = True
    if y1 == y2:
        print(f"Caso #{i}: De novo!")
    elif bazinga == True:
        print(f"Caso #{i}: Bazinga!")
    elif bazinga == False:
        print(f"Caso #{i}: Raj trapaceou!")
