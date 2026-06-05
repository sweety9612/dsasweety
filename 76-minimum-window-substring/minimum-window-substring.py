from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        left = 0
        tdict = Counter(t)
        sdict = defaultdict(int)

        minsub = ""
        mini = float('inf')

        for right in range(len(s)):
            if s[right] in tdict:
                sdict[s[right]] += 1

            # Shrink while window is valid
            while left <= right and all(
                sdict[ch] >= tdict[ch] for ch in tdict
            ):
                subs = s[left:right + 1]

                if len(subs) < mini:
                    mini = len(subs)
                    minsub = subs

                if s[left] in tdict:
                    sdict[s[left]] -= 1

                left += 1

        return minsub