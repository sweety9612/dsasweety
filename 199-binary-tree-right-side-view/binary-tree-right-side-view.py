
from collections import deque
class Solution(object):
    def rightSideView(self, root):
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
            
            res.append(lev[-1])

        return res
        