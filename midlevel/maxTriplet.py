def solution(A):
    """
    :param A: array of integers
    :return: an integer
    """
    # sort them, then just use the last three!
    A.sort()
    print(A)
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        # excepting that two negatives make a positive...
        return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
    else:
        return A[-3] * A[-2] * A[-1]


A=[-1,-1,2,-2,5,6]
print("Max of triplets is:",solution(A))