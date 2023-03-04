#given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If #there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
#For example, given array A such that:

#    A[0] = 4
#    A[1] = 2
#    A[2] = 2
##    A[3] = 5
#    A[4] = 1
#    A[5] = 5
#    A[6] = 8
#the function should return 1, as explained above.



def solution(A):
    n = len(A)
    pre_sum = [0] * (n + 1)
    min_slice_avg = 100000000000
    min_slice_idx = 0

    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + A[i - 1]

        # calculate at least 2 prefix sums
        if i - 2 < 0:
            continue

        # check prev 3 slices if we have calculated 3 prefix sums
        if i >= 3:
            prev_3_slice_avg = (pre_sum[i] - pre_sum[i - 3]) / 3.0

            if prev_3_slice_avg < min_slice_avg:
                min_slice_avg = prev_3_slice_avg
                min_slice_idx = i - 3

        # check prev 2 slices
        prev_2_slice_avg = (pre_sum[i] - pre_sum[i - 2]) / 2.0

        if prev_2_slice_avg < min_slice_avg:
            min_slice_avg = prev_2_slice_avg
            min_slice_idx = i - 2

    return min_slice_idx