# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    bstring = str(bin(N))[2:]
    print (bstring)
    gap = max_gap = 0
    for char in bstring:
        if char == "0":
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0
    print ("Max Gap is :=", max_gap)
    return max_gap
    pass

solution(32)