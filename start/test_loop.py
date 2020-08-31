def loop_sum(num):
    prevNum = 0
    for i in range(num):
        sum = prevNum + i
        print ("Current Number ", i , "Previous Number ", prevNum, "Sum:", sum)
        prevNum = i


loop_sum(10)
#print("output from caculation is:" + str(output))