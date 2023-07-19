while True:
    try:
        n, k = list(map(int, input().split()))
        
        if n == k == 0:
            break
        
        questions = list(map(int, input().split()))
        
        
        frequencyDict = {}
        count = 0
        
        for question in questions:
            frequency = frequencyDict.get(question, 0)
            frequencyDict.update({question: frequency + 1})
            
        for frequency in frequencyDict:
            if frequencyDict.get(frequency, 0) >= k:
                count += 1
                
        print(count)
                    
    except:
        break