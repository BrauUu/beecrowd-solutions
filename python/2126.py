count = 0
while True:
    try:
        n1 = int(input())
        n2 = int(input())
        
        n1 = str(n1)
        n2 = str(n2)
        
        subSeqCount = 0
        pos = 0
        count += 1

        for i in range(len(n2)):
            if n1[0] == n2[i]:
                if n1 == n2[i:i+len(n1)]:
                    subSeqCount += 1
                    pos = i + 1
                    
        print(f'Caso #{count}:')
        
        if subSeqCount == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {subSeqCount}')
            print(f'Pos: {pos}')
            
        print('')
        
    except:
        break
