from collections import defaultdict
class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        count=0
        binmap=defaultdict(int)
        maxone=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            while left<=i and count>k:
                leftbin=nums[left]
                if leftbin==0:
                    count-=1
                left+=1
            maxone=max(maxone,i-left+1)
        return maxone


            
                

                

        