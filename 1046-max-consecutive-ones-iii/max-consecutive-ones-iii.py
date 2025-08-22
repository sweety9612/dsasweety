from collections import defaultdict
class Solution(object):
    def longestOnes(self, nums, k):
        count=defaultdict(int)
        maxones=0
        start=0
        end=0
        while(end<len(nums)):
            count[nums[end]]+=1
            window=end-start+1
            onecount=count[1]
            countdiff=window-onecount
            if countdiff <=k:
                totones=onecount+countdiff
                if totones>maxones:
                    maxones=totones
                end+=1
            else:
                while window-onecount > k:
                    count[nums[start]]-=1
                    start+=1
                    window=end-start+1
                    onecount=count[1]
                end+=1
        return maxones



        
        