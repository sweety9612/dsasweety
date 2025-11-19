import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        flag = 0
        sofarmin = 0
        low = 1                  
        high = max(piles)

        n = len(piles)
        if n == 1:
            return int(math.ceil(float(piles[0]) / h))
        
        while low <= high:
            mid = (low + high) // 2
            
            tothr = 0
            exceed = False
            
            for i in piles:
                tothr += int(math.ceil(float(i) / mid))
               
                
                if tothr > h:
                    exceed = True
                    break
            
            if not exceed:
                sofarmin = mid
                flag = 1
                high = mid - 1     
            else:
                low = mid + 1   
            
        if not flag:
            sofarmin = mid
        
        return sofarmin
