from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        freqMap=defaultdict(int)
        for word in words:
            freqMap[word]+=1
        n=len(words)
        wordBuckets=[[] for _ in range(n+1)]
        for word,freq in freqMap.items():
            wordBuckets[freq].append(word)
        print(wordBuckets)
        res=[]
        for freq in range(n,0,-1):
            ch=[]
            for word in sorted(wordBuckets[freq]):
                res.append(word)
                if len(res)==k:
                    return res
                

        