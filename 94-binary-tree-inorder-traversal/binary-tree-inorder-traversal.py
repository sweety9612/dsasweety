# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res=[]
        stack=[]
        node=root
        while True:
            if not node is None:
                stack.append(node)
                node=node.left
            else:
                if len(stack)==0:
                    break
                node=stack.pop()
                res.append(node.val)
                node=node.right
        return res


        