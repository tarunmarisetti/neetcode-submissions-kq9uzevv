class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford algorithm
        prices=[float('inf')]*n
        prices[src]=0
        for i in range(k+1):
            tempPrices=prices[:]
            for u,v,cost in flights:
                if prices[u]==float('inf'):
                    continue
                if prices[u]+cost<tempPrices[v]:
                    tempPrices[v]=prices[u]+cost
            prices=tempPrices
        return prices[dst] if prices[dst]!=float('inf') else -1

        