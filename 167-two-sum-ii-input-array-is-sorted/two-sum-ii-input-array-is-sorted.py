class Solution(object):
    def twoSum(self, nums, target):
        i,j=0,len(nums)-1
        while i<j:
            cursum=nums[i]+nums[j]
            if cursum<target:
                i+=1
            elif cursum>target:
                j-=1
            else:
                return [i+1,j+1]
        

        