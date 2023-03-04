#For example, you are given integer X = 5 and array A such that:

#  A[0] = 1
#  A[1] = 3
#  A[2] = 1
#  A[3] = 4
#  A[4] = 2
#  A[5] = 3
#  A[6] = 5
#  A[7] = 4
#In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

def solution (X, A):    
    leaves = set()
    for count, leaf in enumerate(A):
        if leaf <= X:   # Only collect the leaves we need to get to X.
            leaves.add(leaf)
            if len(leaves) >= X:
                return count
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))