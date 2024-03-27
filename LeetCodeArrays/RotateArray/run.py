class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
         selectedNum=nums[len(nums)-1]
         nums.remove(selectedNum)
         nums.insert(0,selectedNum)
        print(nums)







