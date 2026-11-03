class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        n = len(height)
        result = 0 
        curr_water = 0 
        for r in range(n):
            if height[r] >= height[l]:
                result+= curr_water 
                curr_water = 0 
                l = r 
            curr_water += height[l]- height[r]
        
        r = n - 1
        curr_water = 0

        for i in range(n - 1, l - 1, -1):
            if height[i] >= height[r]:
                result += curr_water
                curr_water = 0
                r = i
            curr_water += height[r] - height[i]

        return result
       