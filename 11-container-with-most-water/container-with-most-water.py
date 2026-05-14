class Solution(object):
    def maxArea(self, height):
        l,r=0,len(height)-1
        maxarea=0
        while l<r:
            h=min(height[l],height[r])
            maxarea=max(h*(r-l),maxarea)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxarea
            
        


        