while True:
    g, p = list(map(int, input().split()))
    if g == p == 0:
        break
    positionsPerChampionship = []
    for i in range(g):
      positionsPerChampionship.append(list(map(int, input().split())))
    
    s = int(input())
    
    for i in range(s):
        kAndScores = list(map(int, input().split()))
        k = kAndScores[0]
        scores = kAndScores[1:]
        
        resultsBasedInScores = [0 for i in range(p)]
        
        for h in range(len(positionsPerChampionship)):
            for j in range(p): 
                pos = positionsPerChampionship[h][j] - 1   
                if pos < k:             
                    resultsBasedInScores[j] += scores[pos]
         
        res = ''
        max = 0
                    
        for h in range(len(resultsBasedInScores)):
            result = resultsBasedInScores[h]
            if result > max:
                max = result
                res = str(h + 1)
            elif result == max:
                res += ' ' + str(h + 1)
                
        print(res)
            
        
                
        
            