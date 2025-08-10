class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        maxLen = 0
        start = 0
        
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen
