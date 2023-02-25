def solution(a):
    d = {}
    #print (d)
    for e in a:
        if (e in d):
            d[e]+=1
            #print(e)
        else:
            d[e]=1
            #print(e)
        print(d)
    for k,v in d.items():
        if(v%2==1):
            #print(k)
            return k


a = [1,2,3,1,2,3,5]
solution(a)