class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        n=mountainArr.length()
        low=0
        high=mountainArr.length()-1
        increasingslope=0
        decreasingslope=0
        peak=0
        peakflag=0
        res=-1
        resflag=0

        while(low<=high):
            
            mid=(low+high)//2
            num=mountainArr.get(mid)
            if mid<n-1:
                nextval=mountainArr.get(mid+1)
            lowval=mountainArr.get(low)
            highval=mountainArr.get(high)
            if mid>0:
                prevval=mountainArr.get(mid-1)
            print('low:',low,'high',high,'mid:',mid)
            if not peakflag and num>nextval and num>prevval:
                peak=1
                peakflag=1
            elif num<nextval:
                print(num,nextval)
                increasingslope=1
                decreasingslope=0
                peak=0
            else:
                decreasingslope=1
                increasingslope=0
                peak=0
            print('decreasingslope',decreasingslope)
            print('increasingslope',increasingslope)
            print('peak',peak)
            if peak:
                if num==target:
                    return mid
                else:
                    
                    if lowval>target and highval>target:
                        return -1
                    elif lowval==target:
                        return low
                    elif highval==target:
                        return high

                    elif highval<=target and lowval<=target:
                        lowval=mountainArr.get(low+1)
                        highval=mountainArr.get(high-1)
                        if lowval==target:
                            return low+1
                        elif highval == target:
                            res=high-1
                            high=mid-1
                        elif lowval<target:
                            high=mid-1
                        else:
                            low=mid+1
                            

                    elif highval<=target:
                        low=mid+1
                    elif lowval<=target:
                        high=mid-1
                    else:
                        high=mid-1
                print('low:',low,'high',high,'mid:',mid)
            elif increasingslope:
                if num==target:
                    if not resflag:
                        res=mid
                        resflag=1
                    else:
                        res=min(res,mid)
                    if lowval>num:
                        return res
                    else:
                        high=mid-1
                elif num>target:
                    if lowval>target:
                        return res
                    else:
                        if lowval<target and highval<target:
                            lowval=mountainArr.get(low+1)
                            highval=mountainArr.get(high-1)
                            if lowval==target:
                                return low+1
                            elif highval == target:
                                res=high-1
                                

                        high=mid-1
                else:
                    low=mid+1
            else:
                print(low,high,res,num,target,'decres')
                if num==target:
                    if not resflag:
                        res=mid
                        resflag=1
                    else:
                        res=min(res,mid)
                    if lowval<=num:
                        high=mid-1
                    else:
                        return res
                elif num>target:
                    if lowval>target:
                        low=mid+1
                    else:
                        high=mid-1
                        
                        
                else:
                    high=mid-1
        return res


                
                    

        