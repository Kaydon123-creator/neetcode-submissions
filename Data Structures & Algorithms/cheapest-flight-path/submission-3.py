class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        graph = defaultdict(set)

        for source, dest, cost in flights:
            graph[source].add((dest, cost))
        heap = []
        dist = [[float("inf") for _ in range(k+2) ] for _ in range(n)]
        dist[src][0] = 0 
        heapq.heappush(heap, (0,0, src))

        while heap:
            cost, step, node = heapq.heappop(heap)

            if node == dst:
                return cost

            if step >= k + 1:
                continue 
            
            
            for nei, weight in graph[node]:
                if weight + cost < dist[nei][step+1]:
                    dist[nei][step+1] = weight + cost 
                    heapq.heappush(heap, (weight + cost , step+1, nei))
                
        return -1 

                
