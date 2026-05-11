class Solution(object):
    def productExceptSelf(self, nums):
        prefixarr=[1]*len(nums)
        suffixarr=[1]*len(nums)
        prev=1
        for i in range(len(nums)):
            prefixarr[i]=prev
            prev*=nums[i]
        prev=1
        print(prefixarr)
        
        for i in range(len(nums)-1,-1,-1):
            suffixarr[i]=prev
            prev*=nums[i]
        print(suffixarr)
        for i in range(len(nums)):
            nums[i]=prefixarr[i]*suffixarr[i]
        return nums

            

            

        