def solution(a):
    if (len(a)==0): 
        return 1
    if(max(a) == len(a)):
        return len(a)+1
    
    a.sort() 
    for _ in range(1, len(a)+1):
        if _ != a[_-1]:
            return _


def solution(A):
    n = len(A) + 1
    if n == 1:
        return 1
    expected_sum = (n * (n + 1)) // 2
    print(expected_sum)
    return expected_sum - sum(A)


a = [1, 2, 3, 5]
solution(a)