from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        for i in nums:
            if count[i]>len(nums)//2:
                return i
        
        
        