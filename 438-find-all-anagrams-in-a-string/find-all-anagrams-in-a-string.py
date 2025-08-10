class Solution(object):
    def findAnagrams(self, s, p):
        p_sorted = sorted(p)
        k = len(p)
        res = []
        for start in range(len(s) - k + 1):
            window = s[start:start + k]
            if sorted(window) == p_sorted:
                res.append(start)  
        return res



        