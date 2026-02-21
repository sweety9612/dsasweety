class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        candidates.sort()
        def help(start,path,remaining):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                help(i+1,path,remaining-candidates[i])
                path.pop()
        help(0,[],target)
        return res
        