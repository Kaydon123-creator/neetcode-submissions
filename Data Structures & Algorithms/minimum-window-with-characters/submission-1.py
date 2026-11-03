class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        characters_set = set(t)

        frequencies = dict(Counter(t))

        l = 0
       

        result = ""

        for r in range(len(s)):
            if s[r] in frequencies:
                frequencies[s[r]]-=1

            while all(x <= 0 for x in frequencies.values()):

                if not(bool(len(result))) or r - l + 1 < len(result):
                    result = s[l:r+1]
                
                if s[l] in frequencies:
                    frequencies[s[l]]+=1
                l+=1 
            

        return result

            
            



        