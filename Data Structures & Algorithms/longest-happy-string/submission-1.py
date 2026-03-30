class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap=[]
        for count,char in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count!=0:
                heapq.heappush(maxHeap,(count,char))
        
        res=''
        while maxHeap:
            longestCount, longestChar=heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==longestChar:
                if not maxHeap:
                    break
                secondLongestCount, secondLongestChar=heapq.heappop(maxHeap)
                res+=secondLongestChar
                if 1+secondLongestCount<0:
                    heapq.heappush(maxHeap,(1+secondLongestCount, secondLongestChar))
                heapq.heappush(maxHeap,(longestCount, longestChar))
            else:
                res+=longestChar
                if 1+longestCount<0:
                    heapq.heappush(maxHeap,(1+longestCount, longestChar))
        return res

                