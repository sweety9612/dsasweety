class Solution(object):
    def findGCD(self, nums):
        minVal=nums[0]
        maxVal=nums[0]
        for i in nums:
            if i < minVal:
                minVal=i
            if i > maxVal:
                maxVal=i
        
        for i in range(minVal,0,-1):
            print(i,' ',minVal,' ',minVal%i,' ',maxVal%i)
            if minVal % i == 0 and maxVal % i == 0:
                return i
        

        