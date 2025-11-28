from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        dictanagram=defaultdict(list)
        for i in strs:
            print(i)
            key=''.join(sorted(i))
            dictanagram[key].append(i)
        print(dictanagram.values())

        return dictanagram.values()


        
        