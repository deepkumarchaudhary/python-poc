def  Solution(N):
    result = 0
    while (N > 0):
        N = N // 10
        result += 1
    print (result)
    return (result)
    pass


Solution(66)