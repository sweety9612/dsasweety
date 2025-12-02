class Solution(object):
    def findAnagrams(self, s, p):
        n,m=len(s),len(p)
        res=[]
        if m>n:
            return []
        countp={}
        for i in p:
            countp[i]=countp.get(i,0)+1
        window={}
        for i in range(m):
            window[s[i]]=window.get(s[i],0)+1

        if window==countp:
            res.append(0)
        
        for i in range(m,len(s)):
            window[s[i]]=window.get(s[i],0)+1
  
            left=s[i-m]
            window[left]-=1
            if window[left] == 0:
                del window[left]
            if window == countp:
                res.append(i-m+1)
        return res

            

            
                
                

            

        
        