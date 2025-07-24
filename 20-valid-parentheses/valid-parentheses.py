class Solution(object):
    def isValid(self, s):
        arr=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                arr.append(i)
            elif i==')':
                if len(arr)==0:
                    return False
                if arr[-1]=='(':
                    arr.pop()
                else:
                    return False
            elif i==']':
                if len(arr)==0:
                    return False
                if arr[-1]=='[':
                    arr.pop()
                else:
                    return False
            elif i=='}':
                if len(arr)==0:
                    return False
                if arr[-1]=='{':
                    arr.pop()
                else:
                    return False
        return len(arr)==0
        