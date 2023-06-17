while True:
    n, m = list(map(int, input().split()))
    
    if n == m == 0:
        break
    
    noOneHasSolvedAllProblems = 1
    allProblemHasSolved = 0
    noOneProblemWasSolvedByEveryone = 0
    everyoneHasSolvedAtLeastAProblem = 1
    
    problemsSolved = [0 for i in range(m)]
    problemsNotSolvedByEveryone = [0 for i in range(m)]
    
    for i in range(n):
        individualResults = list(map(int, input().split()))
        
        if noOneHasSolvedAllProblems == 1:  
            if individualResults.count(0) == 0:
                noOneHasSolvedAllProblems = 0
                
        if everyoneHasSolvedAtLeastAProblem == 1:
            if individualResults.count(1) == 0:
                everyoneHasSolvedAtLeastAProblem = 0
                
        for g in range(m):
            if individualResults[g] == 1:
                problemsSolved[g] = 1
            else:
                problemsNotSolvedByEveryone[g] = 1
         
        if noOneProblemWasSolvedByEveryone == 0:
            if problemsNotSolvedByEveryone.count(0) == 0:
                noOneProblemWasSolvedByEveryone = 1
                
        if allProblemHasSolved == 0:    
            if problemsSolved.count(0) == 0:
                allProblemHasSolved = 1
    
    sum = noOneHasSolvedAllProblems + allProblemHasSolved + noOneProblemWasSolvedByEveryone + everyoneHasSolvedAtLeastAProblem
    print(sum)
        
        
        
        
        