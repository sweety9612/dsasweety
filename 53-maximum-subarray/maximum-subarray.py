class Solution(object):
    def maxSubArray(self, nums):
        i,j=0,0
        cursum=0
        maxsum=float('-inf')
        while j<len(nums):
            cursum+=nums[j]
            maxsum=max(maxsum,cursum)
            if cursum<0:
                i+=1
                j=i
                cursum=0
            else:
                j+=1
        return maxsum

        