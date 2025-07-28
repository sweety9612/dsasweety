class Solution(object):
    def trap(self, height):
        nxtgrt1=[0]*len(height)
        nxtgrt2=[0]*len(height)
        curmax=height[0]
        finmax=height[0]
        nxtgrt1[0]=0
        for idx in range(1,len(height)):
            if height[idx-1]>curmax:
                curmax=height[idx-1]
            nxtgrt1[idx]=curmax
        curmax=0
        nxtgrt2[len(height)-1]=0
        for revidx in range(len(height)-2,0,-1):
            if height[revidx+1]>curmax:
                curmax=height[revidx+1]
            nxtgrt2[revidx]=curmax
        nxtgrt2[0]=curmax

            
        print(nxtgrt1,'nxtgrt2')
        print(nxtgrt2,'nxtgrt2')
        tot=0
        for i in range(len(height)):
            diff = min(nxtgrt1[i], nxtgrt2[i]) - height[i]
            tot += 0 if diff <0 else diff

        return tot

            
            
        