class Solution(object):
    def nextGreaterElements(self, nums):
        stack=[]
        ans=[-1]*len(nums)
        for i in range(2*(len(nums))-1,-1,-1):
            i=i%len(nums)
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack:
                ans[i]=nums[stack[-1]]
            stack.append(i)
        return ans
        
        