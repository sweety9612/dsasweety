class Solution(object):
    def subsets(self, nums):
        res=[]
        def help(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                help(i+1,path)
                path.pop()
                
        help(0,[])
        return res


        