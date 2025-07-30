class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        countMap={}
        sorted_nums=sorted(nums)
        for i,num in enumerate(sorted_nums):
            if not num in countMap:
                countMap[num]=i
        return [countMap[num] for num in nums]


        