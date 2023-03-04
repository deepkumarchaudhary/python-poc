import itertools
def brute_solution(A):
    for P, Q, R in itertools.combinations(A, 3):
        if (P + Q > R) and (Q + R > P) and (R + P > Q):
            return 1
    return 0


def better_solution(A):
    """Sort before traverse.
    :param A: list[int]
    :return: [int] 1 if there is a triangle, otherwise 0
    """
    is_triangle = lambda P, Q, R: (P + Q > R) and (Q + R > P) and (R + P > Q)

    A.sort()

    for i in range(len(A) - 2):
        if is_triangle(A[i], A[i+1], A[i+2]):
            return 1
    return 0


solution = better_solution
