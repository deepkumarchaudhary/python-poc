def soloution(A):
    A = sorted(A)
    counter = 1
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            counter += 1
            continue
        if counter % 2 == 1:
            return A[i]
        else:
            counter = 1
    print (A[-1])
    return A[-1]
    pass

A = [1,2,3,1,8,2,3]
soloution(A)