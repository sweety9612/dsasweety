class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        dicts={}
        for i in range(len(s)):
            if s[i] not in dicts  and t[i] not in dicts.values():
                dicts[s[i]]=t[i]
        
        arr=[]
        print(dicts,'dicts')
        for i in s:
            arr.append(dicts.get(i," "))
        print(''.join(arr)) 
        if  t!= ''.join(arr):
            return False

        return True
        

        