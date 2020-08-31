# Get the number from user manually 
num = int(input("Enter your favourite number: "))
 
# Initiate value to null
test_num = 0
 
# Check using while loop
 
while(num>0):
  #Logic
  remainder = num % 10
  #print (remainder)
  test_num = (test_num * 10) + remainder
  #print (test_num)
  num = num//10
  print (num)
 
# Display the result
print("The reverse number is : {}".format(test_num))