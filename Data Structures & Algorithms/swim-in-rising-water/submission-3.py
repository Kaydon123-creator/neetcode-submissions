class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap = []
        n = len(grid)
        m = len(grid[0])
        heapq.heappush(heap, (grid[0][0],(0,0)))
        min_time = {(i,j):float("inf") for i in range(n) for j in range(m)}
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        min_time[(0,0)] = grid[0][0] 
        while heap:
            cost, node = heapq.heappop(heap)

            for r,c in directions:
                i = node[0] + r 
                j = node[1] + c
                if n> i >= 0 and m >j>=0 and min_time[(i,j)] > max(cost, grid[i][j]):
                    min_time[(i,j)] =  max(cost, grid[i][j])
                    heapq.heappush(heap,(min_time[(i,j)], (i,j)))
        
        return min_time[(n-1, m-1)] if min_time[(n-1,m-1)] != float("inf") else -1


        