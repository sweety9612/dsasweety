class Solution(object):
    def removeDuplicates(self, nums):
        l,r=0,1
        while r<len(nums):
            if nums[r]==nums[r-1]:
                r+=1
            else:
                nums[l+1]=nums[r]
                l+=1
                r+=1
        return l+1
            


        