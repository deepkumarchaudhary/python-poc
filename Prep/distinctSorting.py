#For example, given array A consisting of six elements such that:
# A[0] = 2    A[1] = 1    A[2] = 1
# A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

def solution(A):
    distinct = set()
    for val in A:
        distinct.add(val)
    return len(distinct)           
pass



A = [2, 1, 1, 2, 3, 1, 4, 4]
print("final",solution(A))