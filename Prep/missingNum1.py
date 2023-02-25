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


a = [1, 2, 3, 5]
b = [0, 1, 2, 3, 4, 5, 6]
solution(a)