def solution(A):
    # write your code in Python 3.6
    #print ("Input List is as follows:")
    #print (A)
    #print ("Sorted list is as follows:")
    A.sort()
    #print(A)
    #print ("Refined list after deletion of duplicate elements is:")
    A = list(dict.fromkeys(A))
    #print (A)
    lengthOfArray=len(A)
    #print ("length of the array is:", lengthOfArray)
    maxValue=max(A)
    if maxValue < 0:
        number=1
    #print("Maximum no from Array is:", maxValue)
    try:
        for i in range(len(A)):
            if A[i] <= 0:
                continue
            elif A[i]+1 != A[i+1]:
                number=A[i]+1
                break
    except IndexError:
        #print("Index out of range error coming up")
        A.extend(((lengthOfArray + 1) - len(A)) * [None])
        number = A[i]+1
    #print ("Positive missing number is: " + str(number))
    return (number)
    
#A =  [1,0, 3, 6, 4, 1, 2]
#A =  [-1,0, -3, 6, 4, 1, -2]
A = [1, 2, 3, 4]
#A= [-3, -1]
#A = [-1, -2, 0, 2]
num=solution(A)
print ("Positive missing number is: ", num)