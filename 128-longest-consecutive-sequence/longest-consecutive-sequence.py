class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0

        for n in numset:
        
            if n - 1 not in numset:
                length = 1
                current = n
                while current + 1 in numset:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
