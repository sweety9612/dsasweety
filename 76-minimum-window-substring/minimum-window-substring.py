class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        dictt = {}
        for ch in t:
            dictt[ch] = dictt.get(ch, 0) + 1

        dicts = {}
        left = 0
        have = 0
        need = len(dictt)

        res = ""
        resLen = float("inf")

        for right in range(len(s)):
            ch = s[right]
            dicts[ch] = dicts.get(ch, 0) + 1

            # check if this char satisfies requirement
            if ch in dictt and dicts[ch] == dictt[ch]:
                have += 1

            # try shrinking window
            while have == need:
                windowLen = right - left + 1
                if windowLen < resLen:
                    res = s[left:right+1]
                    resLen = windowLen

                # remove left char
                leftChar = s[left]
                dicts[leftChar] -= 1
                if leftChar in dictt and dicts[leftChar] < dictt[leftChar]:
                    have -= 1
                left += 1

        return res
