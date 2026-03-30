class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks_sum=sum(matchsticks)
        if matchsticks_sum%4!=0:
            return False
        side_len=matchsticks_sum//4

        matchsticks.sort(reverse=True)
        sides=[0]*4
        def backtrack(i):
            if i==len(matchsticks):
                return True
            for side in range(4):
                if sides[side]+matchsticks[i]<=side_len:
                    sides[side]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[side]-=matchsticks[i]
            return False
        return backtrack(0)
        