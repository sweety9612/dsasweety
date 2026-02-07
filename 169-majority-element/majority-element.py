class Solution(object):
    def majorityElement(self, nums):
        target=len(nums)//2
        count=0
        dictn={}
        for i in nums:
            dictn[i]=dictn.get(i,0)+1
            if dictn[i]>target:
                return i

        

        