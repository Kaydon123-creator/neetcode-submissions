class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(i, path, curr_sum):
            if curr_sum == target:
                result.append(path[:])
                return 
            if i >= len(candidates) or curr_sum > target:
                return
 
            
            path.append(candidates[i])
            backtrack(i + 1, path, curr_sum + candidates[i])
            path.pop()
            while i  < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+=1 
            backtrack(i + 1, path, curr_sum)

            
        
            
        backtrack(0,[], 0)
        return result
        
        