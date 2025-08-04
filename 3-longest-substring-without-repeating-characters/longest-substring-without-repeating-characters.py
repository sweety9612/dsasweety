class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi=0
        i=0
        j=0
       
        sub=""
        word=set()
        print(len(s))
        while(j<len(s)):
            
            if s[j] in word :
                maxi=max(maxi,len(sub))
                sub=""
                word=set()
                i+=1
                j=i
            else:
                word.add(s[j])
                sub+=s[j]
                j+=1
        print(sub,'hh')
        maxi=max(maxi,len(sub))   
        return maxi

            

