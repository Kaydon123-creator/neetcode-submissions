class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        heap = [-value for value in dict(Counter(tasks)).values()]
        heapq.heapify(heap)
        queue = deque([])
        time = 0 
       
        while heap or queue:
            time+=1
            if heap:
                task = -heapq.heappop(heap)
                if task-1 != 0:
                    queue.append((task - 1, n+time))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, -queue.popleft()[0])

        return time




