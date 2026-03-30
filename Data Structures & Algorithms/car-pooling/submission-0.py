class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        min_heap=[]
        curr_capacity=0
        for no_of_passengers, start,end in trips:
            while min_heap and min_heap[0][0]<=start:
               curr_capacity-= heapq.heappop(min_heap)[1]
            curr_capacity+=no_of_passengers
            if curr_capacity>capacity:
                return False
            heapq.heappush(min_heap,[end,no_of_passengers])
        return True

        