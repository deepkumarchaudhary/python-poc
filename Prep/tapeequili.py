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