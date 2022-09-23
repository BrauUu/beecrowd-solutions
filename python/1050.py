ddd = int(input())

states = {
    "Brasilia" : 61,
    "Salvador" : 71,
    "Sao Paulo": 11,
    "Rio de Janeiro": 21,
    "Juiz de Fora": 32,
    "Campinas": 19,
    "Vitoria": 27,
    "Belo Horizonte": 31
}

count = 0

for state in states:
    if states[state] == ddd:
        print(state)
        count+=1

if count == 0:
    print('DDD nao cadastrado')
