"""
https://stackoverflow.com/questions/72172274/python-pothole-fixing-machine
Problem statement

There are a similar versions of this task, but I haven't found answer to this particular one. Basically, there are two roads L1 and L2. The have the same length. The road can consist of a pothole ('X') and a normal concrete ('.'). Your task is to find the most optimal way to cross the road from left to right while finding the maximum number of potholes that can be fixed.

Consider the example:

L1 = '.xxx...x'

L2 = '..x.xxxx'

In this scenario the maximum number of potholes we can fix is 6. 
"""

def solution(L1, L2 ):
    count = 0
    #if 'x' in [L2[0], L1[0]]:
    #    count += 1
    for i in range(1, len(L1)):
        if 'x' not in [L1[i], L2[i]]:
            continue
        if all([L1[i] == 'x', L2[i] == 'x']):
            count += 1
        if ([L1[i], L2[i]] == [L1[i-1], L2[i-1]] ):
            count +=1 
    return count
    pass




#Testing
A = [2, 4, 5, 8, 3]
L1 = 'x...x'
L2 = '..x..'
print("Output of solution is:", solution(L1, L2))
