while True:
    phrase = input()
    
    if phrase == '*':
        break
    
    isTautogram = True
    phraseArr = phrase.split()
    initial = phraseArr[0][0].lower()
    
    for word in phraseArr:
        
        if word[0].lower() != initial:
            isTautogram = False
            break
        
    print("N" if isTautogram == False else "Y")