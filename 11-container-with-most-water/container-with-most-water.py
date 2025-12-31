class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        maxarea=0
        while i<j:
            h=min(height[i],height[j])
            l=j-i
            area=h*l
            maxarea=max(maxarea,area)
            if height[i]==h:
                i+=1
            else:
                j-=1
        return maxarea

        