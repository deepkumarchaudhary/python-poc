#For example, given array A such that:
#  A[0] = 2
#  A[1] = 3
#  A[2] = 1
#  A[3] = 5
#the function should return 4, as it is the missing element.

def solution(A):
    print (A)
    full_array = range(1, len(A) + 2)
    arr = sum(range(1, 2))
    arr1 = sum(range(1, 3))
    arr2 = sum(range(1, 4))
    arr3 = sum(range(1, 5))
    print (arr, arr1, arr2, arr3)
    print(full_array)
    print(sum(full_array))
    print(".....", (sum(full_array) - sum(A)))
    return sum(full_array) - sum(A)
    pass


def solution(a):
    if (len(a)==0): 
        return 1
    if(max(a) == len(a)):
        return len(a)+1
    
    a.sort() 
    for _ in range(1, len(a)+1):
        if _ != a[_-1]:
            return _


def solution1(A):
    n = len(A) + 1
    if n == 1:
        return 1
    expected_sum = (n * (n + 1)) // 2
    print(expected_sum)
    return expected_sum - sum(A)


def solution2(A):
    if (len(A)==0): 
        return 1
    N = len(A)
    my_list = [0] * (N+2)
    missing_element = -1

    for i in range(0, N): 
        my_list[ A[i] ] += 1
        #print(my_list)
    for i in range(1, N+2):
        if my_list[ i ] == 0:
            missing_element = i

    return missing_element
    pass




#a = [1, 2, 3,4, 5, 7]
a = [-1, -3]
print(solution2(a))