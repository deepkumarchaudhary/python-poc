#Two Lane problem (L1, L2)
#count of Potholes is required

def solution(L1, L2 ):
    count = 0
    if 'x' in (L2[0], L1[0]):
        count += 1
    for i in range(1, len(L1)):
        j = i - 1
        if L1[i] == 'x' and L2[i] == 'x':
            count += 1
        elif (L1[i] == 'x' and L2[i] == '.'):
            if (L1[j] == '.' and L2[j] == 'x'):
                continue
            count +=1
        elif (L2[i] == 'x' and L1[i] == '.'):
            if (L1[j] == 'x' and L2[j] == '.'):
                continue
            count += 1
    return count
    pass




#Testing
A = [2, 4, 5, 8, 3]
L1 = 'x...x'
L2 = '..x..'
L3 = '..xx.x.'
L4 = 'x.x.x..'
print("Output of solution is:", solution(L3, L4))