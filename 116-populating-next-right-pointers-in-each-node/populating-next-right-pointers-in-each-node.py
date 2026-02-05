"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        arr=deque()
        if root is None:
            return 
        arr.append(root)
        while arr:
            size=len(arr)
            pnt=None
            for i in range(len(arr)-1,-1,-1):
                arr[i].next=pnt
                pnt=arr[i]

            for i in range(size):
                child=arr.popleft()
                if child.left:
                    arr.append(child.left)
                if child.right:
                    arr.append(child.right)
        return root
                
                
        