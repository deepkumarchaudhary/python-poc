#For example, consider array A such that:
#  A[0] = 3
#  A[1] = 1
#  A[2] = 2
#  A[3] = 4
#  A[4] = 3
#We can split this tape in four places:

#P = 1, difference = |3 − 10| = 7
#P = 2, difference = |4 − 9| = 5
#P = 3, difference = |6 − 7| = 1
#P = 4, difference = |10 − 3| = 7

def solution(A):
    L_sum = A[0]
    R_sum = sum(A[1:])
    min_diff = abs(L_sum - R_sum)
    for i in range (1, len(A) - 1):
        L_sum += A[i]
        R_sum -= A[i]
        diff = abs(L_sum - R_sum)
        if diff < min_diff:
            min_diff = diff
    print (min_diff)
    return min_diff
    pass

a = [1, 2, 3, 5, 6, 8]
solution(a)