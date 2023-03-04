#An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index,
#and the last element of the array is moved to the first place. For example, 
#the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
#(elements are shifted right by one index and 6 is moved to the first place).

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

def solution2(A, K):
    print (A)
    if not len(A):
        return A
    mod_k = (len(A) + K) % len(A)
    print (mod_k)
    if mod_k == 0:
        return A
    head = A[:-mod_k]
    tail = A[len(A) - mod_k:]
    print (head)
    print (tail)
    print (tail + head)
    return tail + head
    pass







A = [3, 8, 9, 7, 6]
K = 2
print(solution(A,K))