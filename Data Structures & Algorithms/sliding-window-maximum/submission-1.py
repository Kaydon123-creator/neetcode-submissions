class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-x,i) for i,x in enumerate(nums[:k])]
        heapq.heapify(heap)
        n = len(nums)
        l = 0 
        result = []
        result.append(-heap[0][0])
        for r in range(k, n):
            if nums[l] == -heap[0][0]:
                heapq.heappop(heap)
            l+=1
            heapq.heappush(heap, (-nums[r],r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            
            result.append(-heap[0][0])
        return result

            

            
            

        
            
        
        