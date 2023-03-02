def solution(N):
    fac = 1
    for i in range(1, N + 1):
        fac *= i
    print(fac)
    return(fac)
    pass


solution(4)