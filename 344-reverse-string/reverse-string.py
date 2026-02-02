class Solution(object):
    def reverseString(self, s):
        i,j=0,len(s)-1
        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        return s
        