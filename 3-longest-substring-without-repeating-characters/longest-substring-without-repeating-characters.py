class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique=set()
        lastindx={}
        i,j=0,0
        maxlen=0
        while j<len(s):
            if s[j] in unique:
                maxlen=max(maxlen,j-i)
                i = max(i, lastindx[s[j]] + 1)

                lastindx[s[j]]=j
                j+=1
            else:
                unique.add(s[j])
                lastindx[s[j]]=j
                j+=1
        maxlen=max(maxlen,j-i)
        return maxlen
                