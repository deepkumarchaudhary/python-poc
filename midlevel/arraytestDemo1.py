def solution(A):
    # write your code in Python 3.6
    A.sort()
    A = list(dict.fromkeys(A))
    lengthOfArray=len(A)
    maxValue=max(A)
    if maxValue < 0:
        number=1
    try:
        for i in range(len(A)):
            if A[i] <= 0:
                continue
            elif A[i]+1 != A[i+1]:
                number=A[i]+1
                break
    except IndexError:        
        A.extend(((lengthOfArray + 1) - len(A)) * [None])
        number = A[i]+1
    return (number)
    
#A =  [1,0, 3, 6, 4, 1, 2]
#A =  [-1,0, -3, 6, 4, 1, -2]
A = [1, 2, 4,5,6]
#A= [-3, -1]
#A = [-1, -2, 0, 2]
num=solution(A)
print ("Positive missing number is: ", num)