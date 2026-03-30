class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks_sum=sum(matchsticks)
        if matchsticks_sum%4!=0:
            return False
        side_len=matchsticks_sum//4

        matchsticks.sort(reverse=True)
        if matchsticks[0]>side_len:
            return False
        sides=[0]*4
        def backtrack(i):
            if i==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]
            for side in range(4):
                if sides[side]+matchsticks[i]<=side_len:
                    sides[side]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[side]-=matchsticks[i]
                if sides[side]==0:
                    break
            return False
        return backtrack(0)
        