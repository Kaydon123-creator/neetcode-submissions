class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        l = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] == 0 :

                max_jump = max(i,max_jump) 
                j = l 
                while j < i:
                    max_jump = max(nums[j]+j,max_jump) 
                    j+=1 

                if max_jump <= i and i!=n-1:
                    return False 
                l = i 
        return True 


            
        