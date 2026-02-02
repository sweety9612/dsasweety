# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        maxi=[0]
        
        def height(root,maxi):
            if root is None:
                return 0
            left=height(root.left,maxi)
            right=height(root.right,maxi)
            maxi[0]=max(maxi[0],left+right)
            return max(left,right)+1
        res=height(root,maxi)
        print(res,' m',maxi)
        return maxi[0]
        