class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq = {}
        window_sum = 0
        max_sum = 0
        
        # Initialize first window
        for i in range(k):
            val = nums[i]
            freq[val] = freq.get(val, 0) + 1
            window_sum += val
        
        if len(freq) == k:
            max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            income = nums[i]
            outgo = nums[i - k]
            
            # Add incoming
            freq[income] = freq.get(income, 0) + 1
            window_sum += income
            
            # Remove outgoing
            freq[outgo] -= 1
            window_sum -= outgo
            
            if freq[outgo] == 0:
                del freq[outgo]
            
            # Check distinct condition
            if len(freq) == k:
                max_sum = max(max_sum, window_sum)
        
        return max_sum
