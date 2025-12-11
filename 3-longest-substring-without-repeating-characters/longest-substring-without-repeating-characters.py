class Solution(object):
    def lengthOfLongestSubstring(self, s):
        word={}
        left=0
        maxlen=0
        for right,ch in enumerate(s):
            if ch in word and word[ch]>=left:
                left=word[ch]+1
            word[ch]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen
