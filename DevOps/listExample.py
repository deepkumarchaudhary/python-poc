def first_last6(nums):
  print(nums[0])
  print(nums[len(nums)-1])
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False
    
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False


def sum3(nums):
  sum = 0
  for i in range (len(nums)):
    sum = sum + nums[i]
  return sum  

def rotate_left3(nums):
    #nums.pop()
    firstItem=nums[0]
    nums=nums[1:]
    print(firstItem)
    nums.append(firstItem)
    print(nums)
    #for i in range (len(nums)):
    #    newArray=nums[i+1]
    #print(newArray)

def max_end(nums):
    maxNo = max(nums)
    print(maxNo)
    for i in range (len(nums)):
        nums[i] = maxNo
    print (nums)

def max_end3(nums):
    if nums[0] > nums[2]:
        maxNo = nums[0]
    else:
        maxNo = nums[2]
    print(maxNo)
    for i in range (len(nums)):
        nums[i] = maxNo
    print (nums)

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return (nums[0]+nums[1])

def middle_way(a, b):
  arr = []
  arr.append(a[1])
  arr.append(b[1])
  return (arr)

def make_ends(nums):
    arr = []
    for i in range (len(nums)):
        if i == 0 or i == (len(nums)-1):
            arr.append(nums[i])
    print (arr)



first_last6([1, 2, 6])# → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False

same_first_last([1, 2, 3]) #→ False
#same_first_last([1, 2, 3, 1]) → True
#same_first_last([1, 2, 1]) → True


sum3([1, 2, 3]) #→ 6
#sum3([5, 11, 2]) → 18
#sum3([7, 0, 0]) → 7


rotate_left3([1, 2, 3])# → [2, 3, 1]
#rotate_left3([5, 11, 9]) → [11, 9, 5]
#rotate_left3([7, 0, 0]) → [0, 0, 7]


max_end3([1, 2, 3])# → [3, 3, 3]
#max_end3([2, 11, 3])
max_end([11, 5, 9]) #→ [11, 11, 11]
#max_end3([2, 11, 3]) → [3, 3, 3]


sum2([1, 2, 3])# → 3
#sum2([1, 1]) → 2
#sum2([1, 1, 1, 1]) → 2


make_ends([1, 2, 3])# → [1, 3]
#make_ends([1, 2, 3, 4]) → [1, 4]
#make_ends([7, 4, 6, 2]) → [7, 2]