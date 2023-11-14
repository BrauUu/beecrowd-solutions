while True:
    try:
        x = input()
        temp = ''
    
        c = {
            '@' : 'a',
            '&' : 'e',
            '!' : 'i',
            '*' : 'o',
            '#' : 'u'
        }

        for letter in x:
            temp += c.get(letter) or letter
            
        print(temp)
    except:
        break