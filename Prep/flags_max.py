#A peak is an array element which is larger than its neighbours. More precisely,
#it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].
#For example, the following array A:
#    A[0] = 1
#    A[1] = 5
#    A[2] = 3
#    A[3] = 4
#    A[4] = 3
#    A[5] = 4
#    A[6] = 1
#    A[7] = 2
#    A[8] = 3
#    A[9] = 4
#    A[10] = 6
#    A[11] = 2
#has exactly four peaks: elements 1, 3, 5 and 10.
#You are going on a trip to a range of mountains whose relative heights are
#represented by array A, as shown in a figure below.




from math import sqrt


def transform(A):
    peak_pos = len(A)
    last_height = A[-1]
    for p in range(len(A) - 1, 0, -1):
        if (A[p - 1] < A[p] > last_height):
            peak_pos = p
        last_height = A[p]
        A[p] = peak_pos
    A[0] = peak_pos


def can_fit_flags(A, k):
    flag = 1 - k
    for i in range(k):
        # we plant the next flag at A[flag + k]
        if flag + k > len(A) - 1:
            return False
        flag = A[flag + k]
    return flag < len(A)  # last flag planted successfully


def solution(A):
    transform(A)
    lower = 0
    upper = int(sqrt(len(A))) + 2
    assert not can_fit_flags(A, k=upper)
    while lower < upper - 1:
        next = (lower + upper) // 2
        if can_fit_flags(A, k=next):
            lower = next
        else:
            upper = next
    return lower