#first
def funct1(name, age):
    print(name,age)
#second
def argFunc(*args):
    count = 0
    for i in args:
        count +=1
        print (i)
    print("No of arguments passed is: ", count)

#Third
def calculation(a, b):
    sum = a + b
    sub = a - b
    print(sum, sub)
    return(sum,sub)
    # Your Code

#Fourth
def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

#Fifth
def outerFun(a,b):
    print(a,b)
    square = a**2
    sum=innerFun(a,b)
    print ("Sum from internal function is: ", sum)

def innerFun(a,b):
    return a+b

#Sixth
def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

#Seventh
def displayStudent(name, age):
    print(name, age)

showStudent = displayStudent
#showStudent("Emma", 26) -- commented for not showing this function value

#Eight
def calcFunc3():
    i = 4
    while (i<30):
        if i%2 == 0:
            print(i)
        i+=1
    
#Nine
def calcFunc4(A):
    print (A)
    print(min(A))
    A.sort()
    print(A)
    print(A[-1])
    #for i in range(len(A)-1):




#Function calling
#name=input("Enter the name:")
#age=int(input("Enter the Age:"))
#funct1(name,age)

#argFunc(20, 40, 60)
#argFunc(80, 100)


#res = calculation(40, 10)
#print(res)
#add, sub = calculation(40, 10)
#print(add)
#print(sub)

#showEmployee("Ben", 9000)
#showEmployee("Ben")

#outerFun(10,20)

#res = calculateSum(10)
#print(res)

#displayStudent("Emma", 26)

#calcFunc3()

#aList = [4, 6, 8, 24, 12, 2]
#calcFunc4(aList)