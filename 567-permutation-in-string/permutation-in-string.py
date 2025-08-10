from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        k=len(s1)
        s1Count=Counter(s1)
        window=Counter(s2[:k-1])
        for start in range(k-1,len(s2)):
            window[s2[start]]+=1
            if window == s1Count:
                return True
            window[s2[start-k+1]]-=1
            if  window[s2[start-k+1]] == 0:
                del  window[s2[start-k+1]]
        return False
        
        