def solution(A):
    #print(A)
    if len(A) == 0:
        return -1
    sort_a = sorted(A)
    #print(sort_a)
    l = len(A) // 2
    #print("median:",l)
    domi_candidate = sort_a[l]
    B=[]
    #print(A.count(domi_candidate))
    if A.count(domi_candidate) > l:
        for i in range(len(A)):
            if A[i] == domi_candidate:
                B.append(i)
        return(B)
    return -1

def solution1(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return -1
    sort_a = sorted(A)
    l = len(A) // 2
    domi_candidate = sort_a[l]
    if A.count(domi_candidate) > l:
        return A.index(domi_candidate)
    return -1



#A=[3,3,3,2,6,-1,3,3]
A=[3, 4, 3, 2, 3, -1, 3, 3]
C=[]
C=solution(A)
print("Dominator index from array is:",C)