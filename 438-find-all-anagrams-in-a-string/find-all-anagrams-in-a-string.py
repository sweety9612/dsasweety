from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        res=[]
        pcount=Counter(p)
        scounter=Counter(s[:len(p)])
        windowsize=len(p)
        if pcount==scounter:
            res.append(0)
        for j in range(len(p),len(s)):
            scounter[s[j]]+=1
            left=s[j-windowsize]
            scounter[left]-=1
            if scounter[left]==0:
                del scounter[left]
            if scounter==pcount:
                res.append(j-windowsize+1)
        return res


        

            

            
                
                

            

        
        