class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        #sort the intervals 

        #sort the queries 

        #for each query loop over the intervals while the start is >= to the query. keep the index at wich we stopped to not loop again on seen queries. 
        #push every spread seen in a min_heap with the end too

        #after doing that while the top of the heap has and end >= the query and a staet lower  we adjust the max . else we pop from the heap 
        original_queries = queries[::]
        query_index_map = {q : i for i,q in enumerate(queries)}
        query_res = {q:-1 for q in query_index_map}
        intervals.sort()
        queries.sort()
        heap = []
        query = [-1]*len(queries)
        i = 0 
        for q in queries:
            while i < len(intervals) and q >= intervals[i][0]:
                l = intervals[i][0]
                r = intervals[i][1]
                heapq.heappush(heap, (r-l+1 , l,r))
                i+=1 

            while heap and (heap[0][2] < q or q < heap[0][1]):
                heapq.heappop(heap)
            if heap :
                query_res[q] = heap[0][0]
       
        return [query_res[q] for q in original_queries]


        

            
            
        