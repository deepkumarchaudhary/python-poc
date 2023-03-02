def solution(N):
    binary_string = str(bin(N))[2:]
    print (binary_string)
    gap = max_gap = 0
    for  i in binary_string:
        if i == "0":
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0   
    return(max_gap)
    Pass




print(solution(1041))