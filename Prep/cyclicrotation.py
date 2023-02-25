def solution(A, K):
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
solution (A,4)


#def solution(A, K):
    # Implement your solution here
#    if not len(A):
#        return 0
#    mod_k = (len(A) + K) % len(A)
#    if mod_k == 0:
#        return A
#    head = A[:- mod_k]
#    tail = A[len(A) - mod_k:]
#    return (tail + head)

#    pass
