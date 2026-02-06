# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    path=[]
    def distanceK(self, root, target, k):
        nodes=[]
        nodelist=self.find(root,target)
        for i in range(len(nodelist)):
            if i==0:
                block=None
            else:
                block=nodelist[i-1]
            nodes.extend(self.printkdown(nodelist[i],k-i,block))
        return nodes
    def find(self,root,target):
        arr=[]
        def help(root,target):
            if root is None:
                return False
            if root == target:
                arr.append(root)
                return True
            left=help(root.left,target)
            if left:
                arr.append(root)
                return True
            right=help(root.right,target)
            if right:
                arr.append(root)
                return right
            return 
        help(root,target)  
        return arr

    def printkdown(self,root,k,block):
        arr=[]
        def help(root,k,block):
            if root is None or root==block or k<0:
                return
            
            if  k==0:
                Solution.path.append(root.val)
                arr.append(root.val)
            help(root.left,k-1,block)
            help(root.right,k-1,block)
            return 
        help(root,k,block)
        print(arr)
        return arr
        
            
        



            

        