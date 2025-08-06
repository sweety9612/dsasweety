from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        prefixsum=0
        res=0
        sumMap=defaultdict(int)
        sumMap[prefixsum]+=1
        for i in nums:
            prefixsum+=i
            res+=sumMap.get(prefixsum-k,0)
            sumMap[prefixsum]+=1
            
            
            

        return res
        