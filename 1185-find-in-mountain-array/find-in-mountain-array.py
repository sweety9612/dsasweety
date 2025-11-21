class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        n=mountainArr.length()
        low=0
        high=n-1
        peak=0
        while(low<=high):
            mid=(low+high)//2
            num=mountainArr.get(mid)
            if mid<n-1:
                nextval=mountainArr.get(mid+1)
            if mid>0:
                prevval=mountainArr.get(mid-1)
            if mid>0 and mid<n-1:
                if num>nextval and num>prevval:
                    peak=mid
                    break
                elif num>nextval:
                    high=mid-1
                else:
                    low=mid+1
            else:
                break
        
        low=0
        high=peak
        print(peak)
        while(low<=high):
            mid=(low+high)//2
            num=mountainArr.get(mid)
            if num==target:
                return mid
            elif num>target:
                high=mid-1
            else:
                low=mid+1
        
        low=peak+1
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            num=mountainArr.get(mid)
            if num==target:
                return mid
            elif num>target:
                low=mid+1
            else:
                high=mid-1

        return -1
