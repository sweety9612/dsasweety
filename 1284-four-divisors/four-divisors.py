import math
class Solution(object):
    
    def sumFourDivisors(self, nums):
        tot=0
        for n in nums:
            divisors=set()
            limit=int(math.sqrt(n))+1
            for i in range(1,limit):
                if n%i==0:
                    divisors.add(i)
                    divisors.add(n//i)
                if len(divisors)>4:
                    break
            if len(divisors)==4:
                tot+=sum(divisors)
        return tot




        