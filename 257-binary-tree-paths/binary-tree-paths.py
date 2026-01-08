# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res=[]
        path=""
        self.dfs(root,res,path)
        return res
    def dfs(self,root,res,path):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            self.dfs(root.left,res,path+str(root.val)+"->")
        if root.right:
            self.dfs(root.right,res,path+str(root.val)+"->")

        

    

        
        