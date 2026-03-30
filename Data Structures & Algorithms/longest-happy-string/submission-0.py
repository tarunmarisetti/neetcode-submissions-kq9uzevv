class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap=[]
        for char, count in [("a",-a),("b",-b),("c",-c)]:
            if count!=0:
                max_heap.append((count,char))
        heapq.heapify(max_heap)
        res=[]

        while max_heap:
            longest_char_count,longest_char=heapq.heappop(max_heap)
            if len(res)>1 and res[-1]==res[-2]==longest_char:
                if not max_heap:
                    break
                second_longest_char_count,second_longest_char=heapq.heappop(max_heap)
                res.append(second_longest_char)
                second_longest_char_count+=1
                if second_longest_char_count!=0:
                    heapq.heappush(max_heap,(second_longest_char_count, second_longest_char))
                heapq.heappush(max_heap,(longest_char_count, longest_char))
            else:
                res.append(longest_char)
                longest_char_count+=1
                if longest_char_count!=0:
                    heapq.heappush(max_heap,(longest_char_count, longest_char))
        return ''.join(res)



            
        