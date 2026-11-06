"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key = lambda x:x.start)

        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)
        number_of_room_booked = 1 
        for inter in intervals[1:]:
            
            while min_heap and min_heap[0] <= inter.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,inter.end)
            number_of_room_booked = max(number_of_room_booked, len(min_heap))
            
        return number_of_room_booked
                
        
        