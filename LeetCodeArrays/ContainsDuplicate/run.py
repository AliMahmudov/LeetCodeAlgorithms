def containsDuplicate(nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
        else:
            return False

print(containsDuplicate([1,2,3,1]))
