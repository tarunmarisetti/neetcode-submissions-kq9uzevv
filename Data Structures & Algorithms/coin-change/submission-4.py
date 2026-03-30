class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        def dfs(remainAmount):
            if remainAmount==0:
                return 0
            if remainAmount<0:
                return float('inf')
            if remainAmount in cache:
                return cache[remainAmount]
            coinsCount=float('inf')
            for coin in coins:
                coinsCount=min(coinsCount, 1+dfs(remainAmount-coin))
            cache[remainAmount]=coinsCount
            return coinsCount
        return dfs(amount) if dfs(amount)!=float('inf') else -1
        