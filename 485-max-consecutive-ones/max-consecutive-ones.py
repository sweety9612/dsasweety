class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ones=0
        maxones=0
        for i in nums:
            if i==1:
                ones+=1
            else:
                maxones=max(ones,maxones)
                ones=0
        maxones=max(ones,maxones)
        return maxones
            
       