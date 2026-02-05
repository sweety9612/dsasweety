class Solution(object):
    def repeatedCharacter(self, s):
        unique=set()
        for i in range(len(s)):
            if s[i] in unique:
                return s[i]

            unique.add(s[i])
        return

        