x = input()

firstIndex = x.find('(')
x = x[(firstIndex if firstIndex != -1 else 0):]

countp1 = 0
countp2 = 0
for c in x:
    if c == '(':
        countp1 += 1
    elif c == ')' and countp2 < countp1:
        countp2 += 1
diff = abs(countp1 - countp2)
print(f'Ainda temos {diff} assunto(s) pendente(s)!' if diff > 0 else 'Partiu RU!')