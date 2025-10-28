class Solution(object):
    def maxArea(self, height):
        n=len(height)
        maxleft=height[0]
        maxright=height[n-1]
        i=0
        j=n-1
        maxarea=(min(maxleft,maxright)*(j-i))
        while i<j:
            maxleft=height[i]
            maxright=height[j]
            maxarea=max(maxarea,(min(maxleft,maxright)*(j-i)))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxarea
            

        