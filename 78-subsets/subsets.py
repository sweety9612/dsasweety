class Solution(object):
    def subsets(self, nums):
        res=[]
        def help(start,arr):
            if len(nums)==0:
                return
            res.append(arr[:])
            for i in range(start,len(nums)):
                arr.append(nums[i])
                help(i+1,arr)
                arr.pop()
        help(0,[])
        return res

        
        