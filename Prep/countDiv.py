#For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 #within the range [6..11], namely 6, 8 and 10.

#def  Solution(N):
#    result = 0
#    while (N > 0):
#        N = N // 10
#       result += 1
#    print (result)
#    return (result)
#    pass

def solution(A,B,K):
    count=0
    while(A<=B):
        if (A%K==0):
            count+=1
        A+=1
    #print(A)
    #print(count)
    return(count)

def solution(A, B, K):
    # write your code in Python 3.6
    
    # need to achieve low complexity O(1)
    # using math equation (low complexity)

    # number of divisible values smaller than B
    num_B = B // K
    # note: take "Math.floor" which is the basic number
    
    # number of divisible values smaller than A
    num_A = A // K
    # note: take "Math.floor" which is the basic number
    
    # number of divisible numbers
    num_divisible = num_B - num_A
    
    # note: plus one (if A % K == 0)
    # because "A" is also divisble 
    plus = 0
    if A % K ==0:
        plus =1
    
    num_divisible = num_divisible + plus
            
    return num_divisible
    pass


print(solution(6, 11, 2))