from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        freqMap=defaultdict(int)
        for c in s:
            freqMap[c]+=1
        n=len(s)
        print(freqMap)
        buckets=[[] for _ in range(n+1)]
        for num,freq in freqMap.items():
            buckets[freq].append(num*freq)
        res=""
        print(buckets)
        for freq in range(n,0,-1):
            ch=""
            for char in buckets[freq]:
                ch+=char
            print(ch,'ch')
            ch="".join(sorted(ch))
            res+=ch
        print(res)
        return res
            

          
        