class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
       
        if len(self.maxheap) == 0 :
            heapq.heappush(self.maxheap, -num)
            return
        
        if -self.maxheap[0] > num :
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        while abs(len(self.maxheap)-len(self.minheap)) > 1:
            if len(self.maxheap) > len(self.minheap):
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        n = len(self.maxheap)
        m = len(self.minheap)
        if n > m:
            return -self.maxheap[0]
        elif n < m :
            return self.minheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2
        
       
        
        
        