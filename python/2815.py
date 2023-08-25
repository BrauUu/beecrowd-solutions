l = input().split()
res = ''

for word in l:
    if len(word) >= 4 and word[:2] == word[2:4]:
        res += word[2:] + ' '
    else:
        res += word + ' '
        
print(res.strip())