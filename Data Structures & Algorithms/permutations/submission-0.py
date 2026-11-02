class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        choices = [False] *n 
        result = []
        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
            for i in range(n):
                if not choices[i]:
                    choices[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    choices[i] = False
        backtrack([])
        return result
        
            