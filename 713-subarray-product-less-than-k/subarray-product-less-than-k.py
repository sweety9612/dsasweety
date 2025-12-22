class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left=0
        subarr=0
        prod=1
        for right in range(len(nums)):
            prod*=nums[right]
            while prod>=k and left<len(nums):
                prod=prod/nums[left]
                left+=1
            
            subarr += (right - left + 1)
        print('r ',right,' ',left)
        print(subarr)
       
        return subarr

            

            



        