class Solution(object):
    def removeStars(self, s):
        stack=[]
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)
        