def solution(S):
    count = 0
    for i in range(0, len(S)):
        if(S[i] == '<'):
            for j in range(i):
                if (S[j]=='.'):
                    count += 1
        elif(S[i] == '>'):            
            for j in range(i+1, len(S)):
                if (S[j]=='.'):
                    count += 1
    return count
    pass


#Testing
A = ".>..."
B = ".>.<.>"
print("Output of solution is:", solution(B))