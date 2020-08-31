def array_count9(nums):
    print (nums)
    count = 0
    for i in range (len(nums)):
        if nums[i] == 9:
            count = count + 1
    print (count)
    return count
  




  
array_count9([1, 2, 9, 9, 9])