def solution(A):
    m = max(A)
    if m < 1:
       return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        print (m + 1)
        return m + 1
    else:
        print (min(D))
        return min(D)
    pass


#a = [1, 3, 6, 4, 1, 2]
a = [-1, -3]
solution(a)