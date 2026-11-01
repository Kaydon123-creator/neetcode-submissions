class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        frequencies_map = sorted(Counter(nums).items(), key = lambda x:-x[1])
        return [num[0] for num in frequencies_map][:k]


        