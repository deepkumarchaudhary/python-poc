def solution(N):
    binary_string = str(bin(N))[2:]
    print (binary_string)
    gap = max_gap = 0
    for char in binary_string:
        if char == "0":
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0
    print (max_gap)
    return max_gap



solution(42)