class Solution(object):
    def maxProfit(self, prices):
        maxi=prices[0]
        mini=prices[0]
        diff=maxi-mini
        for i in prices:
            if i<mini:
                mini=i
                maxi=i
                diff=max(maxi-mini,diff)
            elif i>maxi:
                maxi=i
                diff=max(maxi-mini,diff)
        return diff

            
        
        