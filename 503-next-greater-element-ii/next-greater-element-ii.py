class Solution(object):
    def nextGreaterElements(self, nums):
        arr=[]
        nxtgr1={}
        res=[-1]*len(nums)
        n=2*len(nums)
        size=len(nums)
        for i in range(2*n-1,-1,-1):
            while len(arr)>0 and nums[i%size]>=arr[-1]:
                arr.pop()
            if i<size:
                if len(arr)>0 :
                    res[i]=arr[-1]
        
            
            arr.append(nums[i%size])
        print(res)
        
       
        return res




        