#Introducing new commit
def solution(A):
    # write your code in Python 3.6
    count=0
    for i in range(len(A)):
        for j in range(len(A)):
            if j!=i:
                if A[i]==A[j]:
                    count = count+1
                else:
                    count = count+0

        if count==0:
            print (A[i])
            return A[i]
pass

A = [0,1, 2, 3, 5]
solution(A)