class Solution(object):
    def moveZeroes(self, nums):
        l,r=0,0
        while r<len(nums):
            if nums[r]!=0:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                r+=1
                l+=1
            else:
                r+=1
        return nums
            
            
        