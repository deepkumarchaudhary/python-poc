#A non-empty array A of M integers is given. This array represents consecutive operations:

#if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
#if A[K] = N + 1 then operation K is max counter.
#For example, given integer N = 5 and array A such that:

#    A[0] = 3
#    A[1] = 4
#    A[2] = 4
#   A[3] = 6
#    A[4] = 1
#   A[5] = 4
#    A[6] = 4
#the values of the counters after each consecutive operation will be:

#    (0, 0, 1, 0, 0)
#    (0, 0, 1, 1, 0)
#    (0, 0, 1, 2, 0)
#    (2, 2, 2, 2, 2)
#    (3, 2, 2, 2, 2)
#    (3, 2, 2, 3, 2)
#    (3, 2, 2, 4, 2)
#The goal is to calculate the value of every counter after all operations

def solution(count, operations):
    n = count + 1
    counters = [0] * n
    oldcmax = cmax = 0
    for idx in operations:
        if idx == count + 1:
            oldcmax = cmax
        else:
            if counters[idx] < oldcmax:
                counters[idx] = oldcmax
            counters[idx] += 1
            if counters[idx] > cmax:
                cmax = counters[idx]
    return [max(num, oldcmax) for num in counters[1:]]
    pass


