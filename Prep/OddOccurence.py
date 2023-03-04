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

def solution1(a):
    d = {}
    #print (d)
    for e in a:
        if (e in d):
            d[e]+=1
            #print(e)
        else:
            d[e]=1
            #print(e)
        print(d)
    for k,v in d.items():
        if(v%2==1):
            #print(k)
            return k

def solution3(A):
    n = len(A)
    if A is None or n == 0:
        return 0
    if n == 1:
        return A[0]
    result = 0
    for i in range(0, n):
        result ^= A[i]
    return result

A = [1,2,3,1,8,2,3]
soloution(A)