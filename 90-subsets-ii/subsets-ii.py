class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        def help(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                help(i + 1, path)
                path.pop()
        help(0,[])
        return res
        