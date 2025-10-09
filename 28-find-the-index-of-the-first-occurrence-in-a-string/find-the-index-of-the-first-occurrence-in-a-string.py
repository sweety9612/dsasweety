class Solution(object):
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        i,j=0,m-1
        while j<n:
            word=haystack[i:j+1]
            print(word)
            if word == needle:
                print('word, ',i)
                return i
            i+=1
            j+=1
        return -1