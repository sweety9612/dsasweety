class Solution(object):
    def findMin(self, nums):
        low=0
        sofarmin=nums[0]
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            sofarmin=min(nums[mid],sofarmin)
            if nums[high]<nums[mid]:
                low=mid+1
            else:
                high=mid-1
        sofarmin=min(nums[mid],sofarmin)
        return sofarmin
            
        