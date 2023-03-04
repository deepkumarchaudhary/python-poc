#A permutation is a sequence containing each element from 1 to N once, and only once.
#For example, array A such that:
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#    A[3] = 2
#is a permutation, but array A such that:
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#is not a permutation, because value 2 is missing.

def solution(A):
    N = len(A)

    occurrence = {}
    for i in range(N):
        occurrence[A[i]] = 1
    print(occurrence)

    flag = 1
    for i in range(1, N+1):
        if occurrence.get(i) == 1:
            continue
        else:
            flag = 0

    return flag


#A = [4, 1, 3, 2]
#A = [1,2,3,4]
A = [4,3,1]
# A =
print(solution(A))