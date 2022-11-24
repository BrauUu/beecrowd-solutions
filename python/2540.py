while True:
    try:
        n = int(input())
        answers = input().split()
        
        agreeCount = 0
        disagreeCount = 0
        
        for asnwer in answers:
            if asnwer == '1':
                agreeCount += 1
            elif asnwer == '0':
                disagreeCount += 1
                
        if agreeCount >= (n / 3) * 2:
            print('impeachment')
        else:
            print('acusacao arquivada')
            
    except:
        break