class Solution(object):
    def checkInclusion(self, s1, s2):
        dicts1={}
        for i in s1:
            dicts1[i]=dicts1.get(i,0)+1
        
        i=0
        j=len(s1)-1
        if len(s1)>len(s2):
            return False
        k,word=0,{}
        while k<=j:
            word[s2[k]]=word.get(s2[k],0)+1
            k+=1
        if word==dicts1:
            return True
        j+=1
        while j<len(s2):
            v=s2[j]
            word[v]=word.get(v,0)+1
            word[s2[i]]=word.get(s2[i],0)-1
            if  word[s2[i]]<=0 :
                del word[s2[i]]
            i+=1
            j+=1
            
            if word == dicts1:
                return True
        return False



        