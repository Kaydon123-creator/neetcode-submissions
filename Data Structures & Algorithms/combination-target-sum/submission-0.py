class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(i, path, curr_sum):
            if curr_sum == target:
                result.append(path[:])
                return 
            if i >= len(nums) or curr_sum > target:
                return 

            path.append(nums[i])
            backtrack(i, path, curr_sum + nums[i])
            path.pop()
            backtrack(i + 1, path, curr_sum)

            
        backtrack(0,[], 0)
        return result
        