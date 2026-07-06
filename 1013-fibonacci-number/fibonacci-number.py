class Solution(object):
    def fib(self, n):
        def help1(n):
            if n==0 or n==1:
                return n
            return help1(n-1)+help1(n-2)
        return help1(n)
        