#CyclicRotation
def solution(A):
    #print("Original Array is:")
    #print(A)
    count=0
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i])
            print(A[j])
            if A[i] != A[j+1]:
                count+=1
            else:
                continue
    return(count)
        

A=[0,1,0,1,1]
#count=arrayShift(A)
print("count of passing cars is:", solution(A))







#decimalToBinary(9)