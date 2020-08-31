#First
def testFun():
    print('My', 'Name', 'Is', 'James', sep='**')
    num = 8
    #print("Octal converted value of number is", oct(num))
    print('%o,' % (num))
    print('%.3f' % 458.541315)

#Second
def inputFloat(num):
    i = 0
    floatNumbers = []
    #print("\n")
    print(num)
    while (i < num):
        print("Enter number at location", i, ":")
        item = float(input())
        floatNumbers.append(item)
        print(i)
        i+=1
    print("User List is ", floatNumbers)

#Third
def inputFile():
    count = 0
    with open("test.txt", "r") as fp:
        lines = fp.readlines()
        count = len(lines)
    with open("newFile.txt", "w") as fp:
        for line in lines:
            if (count == 3):
                count -= 1
                continue
            else:
                fp.write(line)
            count-=1
    with open("newFile.txt","r") as fin:
        fin.readlines()
#Function Calling
#testFun()
inputFloat(5)
#inputFile()