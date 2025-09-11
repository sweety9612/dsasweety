from collections import defaultdict
class Solution(object):
    def numIdenticalPairs(self, nums):
        numberMap=defaultdict(int)
        for i in nums:
            numberMap[i]=numberMap.get(i,0)+1
        count=0
        for n in numberMap.values():
            count+=(n*(n-1))//2

        return count
        