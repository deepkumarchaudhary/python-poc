def solution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]
    for i in A[1:]:
        max_slice_ending_here = max(i, max_slice_ending_here+i)
        max_slice = max(max_slice, max_slice_ending_here)
    return max_slice




A=[3,2,-6,4,0]
print("Sum from max slice problem is:", solution(A))