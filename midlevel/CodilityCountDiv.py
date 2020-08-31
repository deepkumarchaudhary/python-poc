#CountDiv
def solution(A,B,K):
    count=0
    while(A<=B):
        if (A%K==0):
            count+=1
        A+=1
    #print(A)
    print(count)
    return(count)


solution(6,18,5)
#print("Count:", num)



