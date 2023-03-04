#The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.
##For example, given:
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#the function should return 5, as explained above.
#(0,1) (0,3) (0,4) (2,3) (2,4)
MAX_PAIRS = int(1e9)
def solution(A):
    east = passes = 0
    for direction in A:
        if direction == 0:
            east += 1
        else:
            passes += east
        if passes > MAX_PAIRS:
            return -1
    return (passes)
    pass

A = [0, 1, 0, 1, 1]
print(solution(A))