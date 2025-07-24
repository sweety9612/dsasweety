class Solution(object):

    def removeDuplicates(self, s):
        arr=[]
        for char in s:
            if len(arr)==0:
                arr.append(char)
            else:
                if char == arr[-1]:
                    arr.pop()
                else:
                    arr.append(char)
        print(arr)
        i=len(arr)-1
        uniqueStr=""
        while i>=0:
            uniqueStr+=arr[i]
            i-=1
        uniqueStr=uniqueStr[::-1]
        
        return uniqueStr

        