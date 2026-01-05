# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        res=[]
        stack=[]
        node=root
        while True:
            if node != None:
                res.append(node.val)
                stack.append(node)
                node=node.left
            else:
                if len(stack)==0:
                    break
                node=stack.pop()
                node=node.right
        return res

        