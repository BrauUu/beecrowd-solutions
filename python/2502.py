while True:
    try:
        c, n = input().split()
        c = int(c)
        n = int(n)
        
        encript1 = input()
        encript2 = input()
        
        encript1 = encript1.upper()
        encript2 = encript2.upper()
        
        for i in range(n):
            phrase = input()
            newPhrase = ''
            
            for i in range(len(phrase)):
            
                pos1 = encript1.find(phrase[i].upper())
                
                if pos1 != -1:
                    newPhrase += encript2[pos1] if phrase[i].isupper() else encript2[pos1].lower()
                    
                pos2 = encript2.find(phrase[i].upper())
                
                if pos2 != -1:
                    newPhrase += encript1[pos2] if phrase[i].isupper() else encript1[pos2].lower()
                elif pos1 == -1 and pos2 == -1:
                    newPhrase += phrase[i]
                    
            print(newPhrase)
        print()
    except:
        break