class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        maxfruitcount = 0
        lastIndex = {}

        for right, fruit in enumerate(fruits):
            lastIndex[fruit] = right

            if len(lastIndex) > 2:
                # find fruit with minimum last index
                removeFruit = min(lastIndex, key=lastIndex.get)
                left = lastIndex[removeFruit] + 1
                del lastIndex[removeFruit]

            maxfruitcount = max(maxfruitcount, right - left + 1)

        return maxfruitcount
