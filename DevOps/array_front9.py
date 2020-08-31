def array_front9(nums):
    print (nums)
    end = len(nums)
    if end > 4:
        end = 4    
    for i in range(end):
        if nums[i] == 9:
            print (i)
            return True
    return False
 






array_front9([1, 2, 9, 3, 4])
#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False