#First
def loopTable(A):
    n = 2
    for i in range(1, 11, 1):
        product = n*i
        print(product)

#Second
def loopCalc(A):
    #n = 2
    i = 1
    sum = 0
    print(A)
    while (i <= A):
        sum = sum + i 
        i+=1
    print(sum)
    
#Third
def sumcalc():
    sum1 = 0
    n = int(input("Please enter number "))
    for i in range(1, n + 1, 1):
        sum1 += i
    print("\n")
    print("Sum is: ", sum1)

#Fourth
def loopvalidation(A):
    print (A)
    for i in range(len(A)-1):
        if A[i] > 150:
            print("Number" , A[i], "is greater than 150..")
            break
        elif A[i] % 5 == 0:
            print (A[i])
            continue

#Fifth
def countNo(num):
    #num = 75869
    count = 0
    while num != 0:
        num //= 10
        count+= 1
    print("Total digits are: ", count)


#Sixth

#list1 = [10, 20, 30, 40, 50]
#list1 = list1[::-1]
#print(list1)
def reverseArray(A):
    start = len(A) - 1
    stop = -1
    step = -1
    for i in range(start, stop, step) :
        print(list1[i])

#Seventh    
def display():
    for num in range(-10, 0, 1):
        print(num)

    


#Function calling........
#loopTable(2)
#loopCalc(5)
#sumcalc()
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#loopvalidation(list1)
#countNo(75869)
#reverseArray(list1)
display()
