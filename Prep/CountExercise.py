def solution(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for i in range(n):
        count [A[i]] += 1
    return count
    pass


def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
            return False

a = [1, 3, 5]
b = [4, 5, 7]

print(solution(a, 3))