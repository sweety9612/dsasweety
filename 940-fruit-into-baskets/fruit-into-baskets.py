from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        fruitdict=defaultdict(int)
        left=0
        maxcount=0
        for i in range(len(fruits)):
            if len(fruitdict)==2 and fruits[i] not in fruitdict:
                maxcount=max(maxcount,sum(fruitdict.values()))
                while left<=i and len(fruitdict)==2:
                    if fruitdict.get(fruits[left]):
                        fruitdict[fruits[left]]-=1
                        if fruitdict[fruits[left]]==0:
                            del fruitdict[fruits[left]]
                    left+=1
                    

            fruitdict[fruits[i]]+=1
        maxcount=max(maxcount,sum(fruitdict.values()))

        return maxcount
    
            



        
