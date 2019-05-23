import heapq

# min and max heap solution
class MedianFinder:
    
    def __init__(self):
        self.median = 0
        self.maxlist = []
        heapq.heapify(self.maxlist)
        self.minlist = []
        heapq.heapify(self.minlist)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxlist, -num) # first put in maxlist
        heapq.heappush(self.minlist, -heapq.heappop(self.maxlist)) # balance
        
        # maintain that maxlist has maximum 1 more item than min list in case minlist has more 
        if len(self.minlist) > len(self.maxlist): 
            heapq.heappush(self.maxlist, -heapq.heappop(self.minlist))
        
    def findMedian(self) -> float:
        if len(self.maxlist) > len(self.minlist): 
            self.median = -self.maxlist[0]
        else:
            self.median = (-self.maxlist[0] + self.minlist[0]) / 2.0
            
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()