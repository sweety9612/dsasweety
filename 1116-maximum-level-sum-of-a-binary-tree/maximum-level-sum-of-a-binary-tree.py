from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        if root is None:
            return ''
        node=deque()
        node.append(root)
        maxval=root.val
        maxlev=1
        lev=1
        while node:
            size=len(node)
            cursum=0
            for _ in range(size):
                child=node.popleft()
                cursum+=child.val
                if child.left:
                    node.append(child.left)
                    
                if child.right:
                    node.append(child.right)
            if cursum>maxval:
                    maxval=cursum
                    maxlev=lev
            lev+=1
        return maxlev
                
        