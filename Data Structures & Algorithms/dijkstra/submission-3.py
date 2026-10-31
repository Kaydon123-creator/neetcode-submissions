class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for x,y,cost in edges:
            graph[x].append((y,cost))
        shortest = {i:float("inf") for i in range(n)}
        shortest[src] = 0
        min_heap = [(src,0)]

        while min_heap:
            node, d = heapq.heappop(min_heap)

            if shortest[node] < d:
                continue

            for neighbor, cost in graph[node]:
                new_dist = d + cost
                if new_dist < shortest[neighbor]:
                    shortest[neighbor] = new_dist
                    heapq.heappush(min_heap,(neighbor, new_dist))
        res = {x:shortest[x] if shortest[x]!=float("inf") else -1 for x in shortest }

        return res
            


