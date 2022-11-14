while True:
    try:
        t = int(input())
        
        expressions = []
        disqualifieds = []
        
        for i in range(t):
            
            expression = input()
            
            expressions.append({
                'value1' : int(expression[:expression.find(" ")]),
                'value2': int(expression[expression.find(" ") + 1 : expression.find('=')]),
                'result' : int(expression[expression.find('=') + 1:]),
            })
            
            
        for i in range(t): 
            answer = input().split()
            
            name = answer[0]
            index = int(answer[1]) - 1
            operator = answer[2]
            
            if operator == '+':
                if expressions[index]['value1'] + expressions[index]['value2'] != expressions[index]['result']:
                    disqualifieds.append(name)
                
            elif operator == '-':
                 if expressions[index]['value1'] - expressions[index]['value2'] != expressions[index]['result']:
                    disqualifieds.append(name)
                
            elif operator == '*':
                 if expressions[index]['value1'] * expressions[index]['value2'] != expressions[index]['result']:
                    disqualifieds.append(name)
                    
            elif operator == 'I':
                 if expressions[index]['value1'] * expressions[index]['value2'] == expressions[index]['result'] or expressions[index]['value1'] + expressions[index]['value2'] == expressions[index]['result'] or expressions[index]['value1'] - expressions[index]['value2'] == expressions[index]['result']:
                     disqualifieds.append(name)
                    
        if len(disqualifieds) < 1:
            print('You Shall All Pass!')
        elif len(disqualifieds) == t:
            print('None Shall Pass!')
        else:
            disqualifieds.sort()
            
            disqualifiedsRes = ''
            
            for name in disqualifieds:
                disqualifiedsRes += name + ' '
                
            print(disqualifiedsRes.strip())
        
    except:
        break