class Solution(object):
    def twoSum(self, nums, target):
        dictnum={}
        for i in range(len(nums)):
            if target-nums[i] in dictnum:
                return [i,dictnum[target-nums[i]]]
            dictnum[nums[i]]=i
        
        