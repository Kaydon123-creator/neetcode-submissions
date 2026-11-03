class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frequencies = defaultdict(int)

        def findMaxChar(map):
            return sorted(map.items(), key = lambda x:x[1], reverse = True)[0][0]
        
        l = 0 
        res = 0
       
    

        for r in range(len(s)):
            frequencies[s[r]]+=1 
            while r - l + 1 - frequencies[findMaxChar(frequencies)] > k:
                frequencies[s[l]]-=1
                l+=1 
                
            res = max(r-l+1, res)

        return res
            
        

        

        