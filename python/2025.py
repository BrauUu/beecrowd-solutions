n = int(input())

jl = len('Joulupukki')

for i in range(n):
    s = input()
    j = 0
    newS = ''
    ind = s.find('oulupukk', j)
    while ind != -1:
        if ind != 0 and s[ind - 1].isalpha():
            newS += s[j:ind-1] + 'Joulupukki'
            j = ind - 1 + jl
        else:
            newS += s[j:ind-2+jl]
            j = ind - 2 + jl
        ind = s.find('oulupukk', j)
    newS += s[j:]
    print(newS)