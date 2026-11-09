class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache
        @cache
        def dp(i):
            if i >= len(s):
                return 1 
            two_num = 0 
            one_num = dp(i+1) if  s[i]!= "0" else 0

            if i < len(s)-1 and s[i]!="0" and int(s[i:i+2]) < 27:
                two_num = dp(i+2)
            return one_num + two_num 

        return dp(0)

            
            


        