class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap=[]# stores[end, passengerCount]
        currCapacity=0
        trips.sort(key=lambda x:x[1]) #sort the trips by the start time
        for passengerCount, start, end in trips:
            while min_heap and min_heap[0][0]<=start:
                currCapacity-=heapq.heappop(min_heap)[1]
            currCapacity+=passengerCount
            if currCapacity>capacity:
                return False
            heapq.heappush(min_heap,(end, passengerCount))
        return True
        