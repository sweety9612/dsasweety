class Solution(object):
    def sortArray(self, arr):
        if not arr:
           return []

        # Step 1: Find the maximum and minimum values
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1  # Handles negative numbers too

        # Step 2: Create and fill the count array
        count = [0] * range_val
        for num in arr:
            count[num - min_val] += 1  # Offset by min_val to handle negatives

        # Step 3: Convert count array to prefix sum for stable sort
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Step 4: Build the output array (traverse input in reverse for stability)
        output = [0] * len(arr)
        for i in reversed(range(len(arr))):
            num = arr[i]
            count[num - min_val] -= 1
            output[count[num - min_val]] = num

        return output
        