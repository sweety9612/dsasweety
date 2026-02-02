class Solution(object):
    def removeDuplicates(self, nums):
        l,r=0,0
        while l<len(nums):
            if nums[l]==nums[r]:
                l+=1
            else:
                r+=1
                nums[r]=nums[l]
                l+=1
        print(r)
        return r+1


        