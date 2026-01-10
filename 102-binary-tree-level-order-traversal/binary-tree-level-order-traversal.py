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
        node=deque()
        res=[]
        node.append(root)
        start=0
        count=0
        lev=[]
        nullchild=0
        val=pow(2,start)-nullchild
        while node:
            size=len(node)
            cur=[]
            for i in range(size):
                curval=node.popleft()
                cur.append(curval.val)
                if curval.left:
                    node.append(curval.left)
                if curval.right:
                    node.append(curval.right)
            res.append(cur)

            
        return res

        