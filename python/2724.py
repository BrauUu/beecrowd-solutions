n = int(input())

for i in range(n):
    t = int(input())
    
    dangerousSolutions = []
    
    for g in range(t):
        dangerousSolutions.append(input())
        
    u = int(input())
    
    for g in range(u):
        experiment = input()
        abort = False
        
        for dangerousSolution in dangerousSolutions:
            index = experiment.find(dangerousSolution)
            if index != -1:
                if (index + len(dangerousSolution) < len(experiment) and (experiment[index + len(dangerousSolution)].isnumeric() == False and experiment[index + len(dangerousSolution)].islower() == False)) or index + len(dangerousSolution) == len(experiment):
                    abort = True
                    print("Abortar")
                    break
                
        if abort == False:
            print("Prossiga")
            
    if i != n - 1:      
        print()