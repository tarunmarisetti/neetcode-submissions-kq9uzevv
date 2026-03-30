class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum=sum(matchsticks)
        sideLen=totalSum//4
        if totalSum/sideLen!=4:
            return False
        # we can return false early if the longest match stick len is greater than sideLen
        matchsticks.sort(reverse=True)
        if matchsticks[0]>sideLen:
            return False
        
        sides=[0]*4
        def backtrack(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i]<=sideLen:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return backtrack(0)
            

        