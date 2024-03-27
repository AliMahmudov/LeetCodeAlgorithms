class Solution(object):
    def removeDuplicates(self,nums):
        for i in nums:
            if nums.count(i)>1:
                nums.remove(i)
        k=len(nums)
        return k,nums
        
    print(removeDuplicates([1,1,2]))


    

    