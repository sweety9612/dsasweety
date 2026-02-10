# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        low=0
        high=len(nums)-1
        def help(nums,low,high):
            mid=(low+high)//2
            if low>high:
                return None
            data=nums[mid]
            left=help(nums,low,mid-1)
            right=help(nums,mid+1,high)
            node=TreeNode(data,left,right)
            return node
        root=help(nums,low,high)
        return root


            
        