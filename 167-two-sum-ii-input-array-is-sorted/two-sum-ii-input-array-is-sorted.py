class Solution(object):
    def twoSum(self, numbers, target):
        dictnum={}
        for i,num in enumerate(numbers):
            dictnum[num]=i
        print(dictnum)
        for i,num  in enumerate(numbers):
            print(i,num)
            val=target-num
            if val in dictnum:
                return [i+1,dictnum[val]+1]
        return

        