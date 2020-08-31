def listconcat(A,B):
    print(A)
    print(B)
    list3 = []
    list3 = [i + j for i, j in zip(A, B)]
    print(list3)
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
list1 = [5, 20, 15, 20, 25, 50, 20]
resList = removeValue(list1, 20)
print(resList)







list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
listconcat(list1,list2)