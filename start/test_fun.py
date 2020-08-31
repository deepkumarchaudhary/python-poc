def calculation(num1 , num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return (num1 + num2)


output=calculation(40,30)
print("output from caculation is:" + str(output))