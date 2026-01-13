# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        if root is None:
            return []
        node=deque()
        node.append(root)
        res=[]
        while node:
            lev=[]
            size=len(node)
            for i in range(size):
                child=node.popleft()
                lev.append(child.val)
                if child.left:
                    node.append(child.left)
                if child.right:
                    node.append(child.right)
            maxval=max(lev)
            res.append(maxval)
        return res

        