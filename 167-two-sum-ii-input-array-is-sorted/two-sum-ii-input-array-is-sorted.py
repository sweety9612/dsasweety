class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while(i<j):
            tot=numbers[i]+numbers[j]
            if tot>target:
                j-=1
            elif tot<target:
                i+=1
            else:
                return [i+1,j+1]

        