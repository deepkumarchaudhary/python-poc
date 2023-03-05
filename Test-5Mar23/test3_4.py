def solution(L1, L2 ):
    count = 0
    if 'x' in [L2[0], L1[0]]:
        count += 1
    for i in range(len(L1)):
        if L1[i] == 'x' and L2[i] == 'x':
            count += 1
        elif (L1[i] == 'x' and L2[i] == '.') or (L2[i] == 'x' and L1[i] == '.'):
            count +=1
        else:
            pass
    return count



#Testing
A = [2, 4, 5, 8, 3]
L1 = '..xx.x.'
L2 = 'x.x.x..'
print("Output of solution is:", solution(L1, L2))