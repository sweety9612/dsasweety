class Solution(object):
    def numDecodings(self, s):
        
        memo = {}
        
        def help(i):
            # Reached end
            if i == len(s):
                return 1
            
            # Leading zero invalid
            if s[i] == '0':
                return 0
            
            # Cached result
            if i in memo:
                return memo[i]
            
            # Single digit
            count = help(i + 1)
            
            # Double digit
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += help(i + 2)
            
            memo[i] = count
            return count
        
        return help(0)
