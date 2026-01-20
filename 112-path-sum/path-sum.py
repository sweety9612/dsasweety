# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        tot=0
        def helper(root,tot):
            if root is None:
                return False
            tot+=root.val
            if root.left is None and root.right is None:
                if tot==targetSum:
                    return True
                else:
                    return False
            
            
            print(tot)
            return (helper(root.left,tot) or helper(root.right,tot))
        return helper(root,tot)

        