class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr=[]
        res=[0]*len(nums1)
        nxtgreater={}
        nums2=nums2[::-1]
        for i in range(len(nums2)):
            while len(arr)>0 and  nums2[i]>=arr[-1]:
                arr.pop()
            if len(arr)>0:
                nxtgreater[nums2[i]]=arr[-1]
            else:
                nxtgreater[nums2[i]]=-1
            arr.append(nums2[i])
        print(nxtgreater)
        for j in range(len(nums1)):
            res[j]=nxtgreater.get(nums1[j])
        return res

            

            
            
            
            
                

