def solution(L1, L2 ):
    count = 0
    #if 'x' in [L2[0], L1[0]]:
    #    count += 1
    for i in range(1, len(L1)):
        if 'x' not in [L1[i], L2[i]]:
            continue
        if all([L1[i] == 'x', L2[i] == 'x']):
            count += 1
        if ([L1[i], L2[i]] == [L1[i-1], L2[i-1]] ):
            count +=1 
    return count
    pass




#Testing
A = [2, 4, 5, 8, 3]
L1 = 'x...x'
L2 = '..x..'
print("Output of solution is:", solution(L1, L2))