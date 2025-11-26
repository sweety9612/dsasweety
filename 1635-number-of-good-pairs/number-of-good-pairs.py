class Solution(object):
    def numIdenticalPairs(self, nums):
        numdict={}
        for i in nums:
            numdict[i]=numdict.get(i,0)+1
        
        totcount=0
        print('numdict ',numdict)
        for i,val in numdict.items():
            print(val)
            totcount+=(val*(val-1))//2
        return totcount



        