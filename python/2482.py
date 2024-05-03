n = int(input())
translates = {}
for _ in range(n):
    language = input()
    translate = input()
    translates.update({language: translate})

m = int(input())
for _ in range(m):
    name = input()
    language = input()
    print(name)
    print(translates[language] + '\n')
