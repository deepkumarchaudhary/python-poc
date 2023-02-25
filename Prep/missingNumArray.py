def solution(a):
    if (len(a)==0): 
        return 1
    if(max(a) == len(a)):
        return len(a)+1
    
    a.sort() 
    for _ in range(1, len(a)+1):
        if _ != a[_-1]:
            return _


a = [1, 2, 3, 5]
solution(a)