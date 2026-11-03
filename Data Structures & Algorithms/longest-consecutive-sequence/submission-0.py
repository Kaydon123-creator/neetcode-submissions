class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0 
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            elem = num
            ans = 1
            while elem + 1 in set_nums:
                ans+=1
                elem += 1 
            res = max(ans, res)
        return res
                
            

        