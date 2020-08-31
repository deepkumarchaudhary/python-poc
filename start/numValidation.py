def numbervalidation(num):
    print ("Original number is: ", num)
    reverseNo = 0
    while (num > 0):
        reminder = num % 10
        reverseNo= (reverseNo*10) + reminder
        num = num // 10
    print(reverseNo)
    if ( num == reverseNo):
        return True
    return False
    
print("The original and reverse number is the same:", numbervalidation(121))