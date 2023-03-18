n = int(input())

for i in range(n):
    l = int(input())
    flag = False
    lang = ''
    otherLang = ''
    for g in range(l):
        if g == 0:
            lang = input()
        else:
            otherLang = input()
            if lang != otherLang:
                flag = True
        
    if flag == True:
        print("ingles")
    else:
        print(lang)