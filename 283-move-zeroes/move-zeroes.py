class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while(j<len(nums)):
            if nums[j]==0:
                j+=1

            else:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
        return i+1
        
        