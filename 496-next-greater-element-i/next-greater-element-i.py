class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr=[]
        res=[]
        nums2=nums2[::-1]
        for i in nums1:
            j=0
            arr=[]
            while nums2[j]!=i:
                arr.append(nums2[j])
                j+=1

            val=-1
            
            while arr and arr[-1]<=i:
                arr.pop()

            if arr and arr[-1]>i:
                val=arr[-1]
            res.append(val)
        
        return res


        
        