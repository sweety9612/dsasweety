# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        res=deque()
        res.append(root)
        output=[]
        while res:
            size=len(res)
            lev=[]
            for i in range(size):
                popval=res.popleft()
                lev.append(popval.val)
                if popval.left:
                    res.append(popval.left)
                if popval.right:
                    res.append(popval.right)
            output.append(lev)
        return output
                
        


        