def testArray2(A,B):
    print(A)
    print(B)
    C = []    
    for i in range(len(A)):
        if (A[i] % 2 != 0):
            C.append(A[i])
        #else:
        #    pass
    print (C)
    for i in range(len(B)):
        if (B[i] % 2 == 0):
            C.append(B[i])
            #C.append(B[i])
        #else:
        #    pass
        print(C)
        return(C)
    



A=[10, 20, 23, 11, 17]
B=[13, 43, 24, 36, 12]
testArray2(A,B)