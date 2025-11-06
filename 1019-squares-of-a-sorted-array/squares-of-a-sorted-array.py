class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)):
            nums[i]=(nums[i]*nums[i])
        
        return nums
        