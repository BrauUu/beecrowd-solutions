cpf = input()

start, end = cpf.split("-")
start = start.split(".")

for num in start:
    print(num)
    
print(end)