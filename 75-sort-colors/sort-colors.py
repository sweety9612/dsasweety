class Solution(object):
    def sortColors(self, nums):
        l,r,m=0,len(nums)-1,0
        while m<=r:
            if nums[m]==0:
                temp=nums[l]
                nums[l]=nums[m]
                nums[m]=temp
                l+=1
                m+=1
            elif nums[m]==2:
                temp=nums[r]
                nums[r]=nums[m]
                nums[m]=temp
                r-=1
            else:
                m+=1
        return nums
            
        