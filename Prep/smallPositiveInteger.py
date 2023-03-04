#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 3], the function should return 4.
#Given A = [−1, −3], the function should return 1.

def solution(A):
    n = len(A)
    counter = [0] * n
    for i in range (0, n):
        if (A[i] > 0) and (A[i] <= n):
            counter[A[i] - 1] += 1
            #print(counter[i])

    for i in range(0, len(counter)):
        if (counter[i] == 0):
            return i + 1
    return n  + 1
    pass

A = [1, 3, 6, 4, 1, 2]
print(solution(A))
#solution(A)
