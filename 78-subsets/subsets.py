class Solution(object):
    


    def subsets(self, nums):
        ans=[]
        def helper(start,nums,ans,arr):
            if start==len(nums):
                ans.append(arr[:])
                return 
            arr.append(nums[start])
            helper(start+1,nums,ans,arr)
            arr.pop()
            helper(start+1,nums,ans,arr)
            
        helper(0,nums,ans,[])
        return ans
      