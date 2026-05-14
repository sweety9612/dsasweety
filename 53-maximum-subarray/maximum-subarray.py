class Solution(object):
    def maxSubArray(self, nums):
        cursum=0
        maxsum=float('-inf')
        for i in nums:
            cursum+=i
            maxsum=max(cursum,maxsum)
            if cursum<0:
                cursum=0
        return maxsum



        