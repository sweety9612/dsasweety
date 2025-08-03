class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        area=0
        maxarea=0

        while i<j:
            minh=min(height[i],height[j])
            wid=j-i
            area=minh*wid
            maxarea=max(maxarea,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxarea
            

        