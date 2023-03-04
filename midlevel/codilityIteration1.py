#CyclicRotation
def arrayShift(A,K):
    
    print("Original Array is:")
    print(A)
    old = A
    new = [0]*len(A)
    print(new)
    for i in range(K):
        new[0]=old[-1]    
        new[1:] = old[:-1]
        old = new.copy()
    print ("New Array is:")
    print (new)
    return new

        

A=[1,2,4,7]
arrayShift(A,3)







#decimalToBinary(9)