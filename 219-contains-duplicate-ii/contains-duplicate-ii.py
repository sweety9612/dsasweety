class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dictnums={}
        for i,val in enumerate(nums):
            
            if val not in dictnums:
                dictnums[val]=i
            else:
                print(i,' ',dictnums[val])
                print(i-dictnums[val],'jhjcs')
                if (i-dictnums[val])<=k:
                    return True
                else:
                    dictnums[val]=i

        
        return False
        