class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        taken = [0]*len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[::])
            
            for i in range(len(nums)):
                if taken[i] == 0:
                    taken[i] = 1 
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    taken[i] = 0 
        backtrack([])
        return result
                

                




                

        