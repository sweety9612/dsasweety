class Solution(object):
    def threeSum(self, nums):
        nums.sort() # [-4,-1,-1,0,1,2]--
        res=set()
        for i in range(len(nums)-2):
            tarsum=0-nums[i]
            j=i+1
            k=len(nums)-1
            cursum=0
            while j<k:
                cursum=nums[k]+nums[j]
                if cursum<tarsum:
                    j+=1
                elif cursum>tarsum:
                    k-=1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    k-=1
                    j+=1
        print(res)
        return list(res)






        