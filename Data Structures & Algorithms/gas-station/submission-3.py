class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum of gas is less than sum of cost then we cant reach every station
        if sum(cost)>sum(gas):
            return -1
        
        total=0
        start=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                start=i+1
                total=0
        return start
