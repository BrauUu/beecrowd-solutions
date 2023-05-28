while True:
    n, k, m = list(map(int, input().split()))
    
    if n == k == m == 0:
        break
    
    queue = [i for i in range(1, n + 1)]
    res = ''
    
    clockwisePos = (k % n if k % n != 0 else n) - 1
    counterclockwisePos = n - (m % n if m % n != 0 else n)
    
    while len(queue) > 1:
        applicant01 = queue[clockwisePos]
        applicant02 = queue[counterclockwisePos]
        
        if applicant01 != applicant02:
            res += (3 - len(str(applicant01))) * ' ' + str(applicant01) + (3 - len(str(applicant02))) * ' ' + str(applicant02) + ','
            queue.pop(clockwisePos)
            clockwisePos -= 1
            if clockwisePos < counterclockwisePos:
                queue.pop(counterclockwisePos - 1)
                counterclockwisePos -= 1
            else:
                queue.pop(counterclockwisePos)
                clockwisePos -= 1
        else:
            res += (3 - len(str(applicant01))) * ' ' + str(applicant01) + ','
            queue.pop(clockwisePos)
            clockwisePos -= 1
        
        if len(queue) == 0:
            break
        
        temp = k % len(queue)
        clockwisePos += temp 
        if clockwisePos >= len(queue):
            clockwisePos -= len(queue)
        elif clockwisePos < 0:
            clockwisePos += len(queue)
            
        temp = m % len(queue)
        counterclockwisePos -= temp
        if counterclockwisePos < 0:
            counterclockwisePos += len(queue)
        elif counterclockwisePos >= len(queue):
            counterclockwisePos -= len(queue)
    
    if len(res) > 0 and res[len(res) - 1] == ',' and len(queue) == 0:
        res = res[:len(res) -1]
    print(res + str((3 - len(str(queue[0]))) * ' ' + str(queue[0]) if len(queue) > 0 else ''))
            
            