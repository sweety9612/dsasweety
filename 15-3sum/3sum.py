class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate 'a'

            a = nums[i]
            j, k = i + 1, len(nums) - 1

            while j < k:
                b, c = nums[j], nums[k]
                tot = a + b + c

                if tot < 0:
                    j += 1
                elif tot > 0:
                    k -= 1
                else:
                    triplets.append([a, b, c])
                    # Skip duplicates for b and c
                    while j < k and nums[j] == b:
                        j += 1
                    while j < k and nums[k] == c:
                        k -= 1

        return triplets
