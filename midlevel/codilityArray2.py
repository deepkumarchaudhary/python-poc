#OddOccurrencesInArray
def solution1(A):
   result = 0
   for number in A:
     result ^= number
   print(result)
   return result

        
def solution2(A):     
    if len(A) == 1:
         return A[0]
    A = sorted(A)       # O(n*log(N) or N)
    for i in range(0 , len (A) , 2): # O(N)
         if i+1 == len(A):
             print(A[i])
             return A[i]
         if A[i] != A[i+1]:
             print(A[i])
             return A[i]
    
# O(N*log(N) or O(N))

def solution3(A):     
    if len(A) == 1:
         return A[0]
    A = sorted(A)
    for i in range(0 , len (A) , 2):
         if i+1 == len(A):
             print(A[i])
             return A[i]
         if A[i] != A[i+1]:
             print(A[i])
             return A[i]

A=[9,3,9,3,9,7,9]
solution1(A)
solution2(A)
solution3(A)








#decimalToBinary(9)