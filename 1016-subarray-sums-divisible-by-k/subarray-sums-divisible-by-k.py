from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefSum=0
        mapPref=defaultdict(int)
        mapPref[0]+=1
        res=0
        for i in nums:
            prefSum+=i
            res+=mapPref.get(prefSum%k,0)
            mapPref[prefSum%k]+=1
        return res

        