class Solution(object):
    def thirdMax(self, nums):
        unique = set(nums)
        fm, sm, tm = float('-inf'), float('-inf'), float('-inf')
        
        for i in unique:
            if i > fm:
                tm = sm
                sm = fm
                fm = i
            elif i > sm:
                tm = sm
                sm = i
            elif i > tm:
                tm = i
        
        return tm if tm != float('-inf') else fm