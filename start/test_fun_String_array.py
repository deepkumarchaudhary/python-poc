def stringManipulation(str):
    print (str)
    for i in range (0, len(str)-1, 8):
        print("index[",i,"]", str[i] )
    #product = num1 * num2
    #if product <= 1000:
    #    return product
    #else:
    #    return (num1 + num2)


inputstring = "Deepak"
print("original string is:", inputstring)
print("printing only even index chars")
stringManipulation(inputstring)
