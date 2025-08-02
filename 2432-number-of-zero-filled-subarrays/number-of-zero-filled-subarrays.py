class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        zero_streak = 0

        for num in nums:
            if num == 0:
                zero_streak += 1
                count += zero_streak
            else:
                zero_streak = 0

        return count
        