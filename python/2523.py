while True:
    try:
        abc = input()
        
        if len(abc) < 1:
            break
        
        alphabet = []
        for letter in abc:
            alphabet.append(letter)
            
        n = int(input())
        
        indexes = input().split()
        
        word = ''
        
        for index in indexes:
            word += alphabet[int(index) - 1]
            
        print(word)
        
    except:
        break