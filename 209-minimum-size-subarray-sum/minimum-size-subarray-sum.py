class Solution(object):
    def minSubArrayLen(self, target, nums):
        subsum=0
        cursum=nums[0]
        start=0
        maxlen=len(nums)
        curlen=0
        end=0
        while end < len(nums) and start<len(nums):
            
            if cursum == target:
                print(target," end ",end," start ",start)
                curlen=(end-start)+1
                if curlen<maxlen:
                    maxlen=curlen
                cursum-=nums[start]
                start+=1
                
            elif cursum>target:
                while start < len(nums) and cursum >target :
                    curlen=(end-start)+1
                    if curlen<maxlen:
                        maxlen=curlen
                    cursum-=nums[start]
                    start+=1
                
            else:
                end+=1
                if end < len(nums):
                    cursum+=nums[end]
                
            print(cursum,' cursum')
        if curlen<maxlen:
            maxlen=curlen
        return maxlen



        