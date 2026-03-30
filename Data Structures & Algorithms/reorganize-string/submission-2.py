class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap={}
        for char in s:
            if char not in freqMap:
                freqMap[char]=0
            freqMap[char]+=1
        max_heap=[(-val,char) for char, val in freqMap.items()]
        heapq.heapify(max_heap)
        res=''
        while len(max_heap)>1:
            freq1,char1=heapq.heappop(max_heap)
            freq2,char2=heapq.heappop(max_heap)
            res+=char1+char2
            if freq1+1<0:
                heapq.heappush(max_heap,(freq1+1, char1))
            if freq2+1<0:
                heapq.heappush(max_heap,(freq2+1, char2))
        if max_heap:
            freq,char=heapq.heappop(max_heap)
            if freq+1<0:
                return ""
            res+=char
        return res
