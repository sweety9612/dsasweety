class Solution(object):
    def maxSubArray(self, nums):
        maxsum=nums[0]
        cursum=0
        for i in nums:
            cursum+=i
            if cursum>maxsum:
                maxsum=cursum
            if cursum<0:
                cursum=0
            
        return maxsum