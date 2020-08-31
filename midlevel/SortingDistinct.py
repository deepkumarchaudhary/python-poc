def solution(A):
    #print(len(A))
    A = list(dict.fromkeys(A))
    return (len(A))
    #print("distinct count from array is:", len(A))

A = [2,1,1,2,3,1]
print("Distinct no count is:", solution(A))
