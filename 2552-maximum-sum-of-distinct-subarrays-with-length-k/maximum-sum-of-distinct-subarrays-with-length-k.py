class Solution(object):
    def maximumSubarraySum(self, nums, k):
        from collections import defaultdict
        
        counts = defaultdict(int)
        cursum = 0
        maxsum = 0
        
        # Initialize first window
        for i in range(k):
            counts[nums[i]] += 1
            cursum += nums[i]
        
        if len(counts) == k:
            maxsum = cursum
        
        # Slide the window
        for start in range(k, len(nums)):
            # Remove outgoing element
            out_num = nums[start - k]
            counts[out_num] -= 1
            if counts[out_num] == 0:
                del counts[out_num]
            cursum -= out_num
            
            # Add incoming element
            in_num = nums[start]
            counts[in_num] += 1
            cursum += in_num
            
            # Check uniqueness
            if len(counts) == k:
                maxsum = max(maxsum, cursum)
        
        return maxsum
