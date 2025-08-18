from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        from collections import defaultdict
        count = defaultdict(int)
        start = 0
        max_count = 0
        max_len = 0

        for end in range(len(s)):
            count[s[end]] += 1
            max_count = max(max_count, count[s[end]])

            # Check if window is valid
            while (end - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
            


        