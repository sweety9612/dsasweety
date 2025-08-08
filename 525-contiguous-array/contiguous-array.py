from collections import Counter
from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        prefixsumMap={0:-1}
        prefixSum=0
        maxLen=0
        for i,num in enumerate(nums):
            if num==0:
                prefixSum-=1
            else:
                prefixSum+=1
            if prefixSum in prefixsumMap:
                maxLen=max(maxLen,i-prefixsumMap[prefixSum])
            else:
                prefixsumMap[prefixSum]=i
        return maxLen







        
        