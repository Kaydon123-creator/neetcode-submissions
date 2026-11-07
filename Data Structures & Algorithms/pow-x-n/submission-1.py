from functools import cache

class Solution:
    def myPow(self, x: float, n: int) -> float:

        @cache
        def divide_mul(x, n):
            if n < 0:
                return 
            if n <= 2:
                return x**n

            return divide_mul(x,n//2)*divide_mul(x,n-(n//2))

    
        return divide_mul(x,n) if n > 0 else divide_mul(1/x, -n)
        