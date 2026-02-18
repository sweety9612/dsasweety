class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        def help(start,path,remaining):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0:
                return
            for choice in range(start,len(candidates)):
                path.append(candidates[choice])
                help(choice,path,remaining-candidates[choice])
                path.pop()
            
        help(0,[],target)
        return res