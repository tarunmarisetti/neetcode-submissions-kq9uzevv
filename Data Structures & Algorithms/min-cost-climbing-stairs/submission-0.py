class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        cost.append(0)
        one,two=cost[-2],cost[-1]
        for i in range(len(cost)-3, -1, -1):
            temp=one
            one=cost[i]+min(one,two)
            two=temp
        return min(one,two)

        
        