def solution(A, K):
    # Implement your solution here
    if not len(A):
        return A
    print("Original Array - ", A)
    old_Array = A
    print (A[1:])
    print(A[:-1])
    new_Array = [0] * len(A)
    print ("New Array - ", new_Array)
    for i in range(K):
        new_Array[0] = old_Array[-1]
        new_Array[1:] = old_Array[:-1]
        old_Array = new_Array.copy()
    print("New Array is:-" ,new_Array)
    return(new_Array)
    pass








A = [3, 8, 9, 7, 6]
K = 2
print(solution(A,K))