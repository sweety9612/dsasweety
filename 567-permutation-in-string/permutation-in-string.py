from collections import Counter
from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1count=Counter(s1)
        windowsize=len(s1)
        j=windowsize
        subword=s2[:len(s1)]
        dicts2=Counter(subword)
        print(dicts2,'dfsf')
        if dicts2==s1count:
            return True

        while j<len(s2):
            dicts2[s2[j]]+=1
            left=s2[j-windowsize]
            dicts2[left]-=1
            if dicts2[left]<=0:
                del dicts2[left]
            if dicts2==s1count:
                return True
            j+=1

        return False


        



        