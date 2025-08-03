class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        addval=0
        while(j<len(numbers)):
            addval=numbers[i]+numbers[j]
            if addval>target:
                j-=1
            elif addval<target:
                i+=1
            else:
                return [i+1,j+1]
        return [i+1,j+1]


        