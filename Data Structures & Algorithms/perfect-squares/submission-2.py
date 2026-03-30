class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares=[]
        for i in range(1,n+1):
            if i**2 <=n:
                perfectSquares.append(i**2)
            else:
                break
        print(perfectSquares)

        cache={}
        def dfs(index, remain):
            
            if index==len(perfectSquares):
                return float('inf')
            if remain==0:
                return 0
            if (index, remain) in cache:
                return cache[(index, remain)]
        
            if remain-perfectSquares[index]>=0:
                consider=1+dfs(index, remain-perfectSquares[index])
                skip=dfs(index+1,remain)
                cache[(index, remain)]= min(consider, skip)
            else:
                cache[(index, remain)]=float('inf')
            return cache[(index, remain)]
        return dfs(0,n)

        