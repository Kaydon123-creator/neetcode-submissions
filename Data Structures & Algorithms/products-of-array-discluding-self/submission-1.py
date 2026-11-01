class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = right = 1 
        result = [0] * len(nums)
        for i,num in enumerate(nums):
            result[i] = left
            left*= num 
        for i,num in enumerate(nums[::-1]):
        
            result[len(nums)-1-i]*=right 
            right*=num 
        return result

        