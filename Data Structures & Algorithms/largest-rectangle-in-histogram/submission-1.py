class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i 
            while stack and stack[-1][0] > height:
                value , index  = stack.pop()
                start = index
                max_area = max(max_area , value * (i-start))
            stack.append((height, start))
        
        end = len(heights)
        while stack :
            value, index = stack.pop()
            max_area = max(value*(end-index), max_area)
        return max_area
