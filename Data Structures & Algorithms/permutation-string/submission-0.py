class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s2)
        frequencies_list = [0]*26
        for c in s1:
            frequencies_list[ord(c)%26]+=1

        l = 0 
        for r in range(n):
            frequencies_list[ord(s2[r])%26]-=1
            while r - l + 1 > len(s1):
                frequencies_list[ord(s2[l])%26]+=1 
                l+=1 
            if all(x == 0 for x in frequencies_list):
                return True
            
        return False 
        
            
                
        