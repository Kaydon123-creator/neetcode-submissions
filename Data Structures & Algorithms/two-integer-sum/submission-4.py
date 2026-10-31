class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map ={}

        for i,num in enumerate(nums):
            if target - num in index_map and index_map[target - num]!=i:
                return [index_map[target - num],i]

            if num not in index_map:
                index_map[num] = i 
        return []
            

        