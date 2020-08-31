def solution(X):
    #print(X)
    if X > 1:
        for i in range(2, X//2):
            if ( X % i ) == 0 :
                return False
            else:
                return True
    #if input number is 
    else:
        return False

print("Prime number validation:",solution(11))