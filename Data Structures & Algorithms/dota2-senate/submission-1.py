class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque()
        D=deque()
        n=len(senate)
        for i,char in enumerate(senate):
            if char=='R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            rIndx, dIndx=R.popleft(), D.popleft()
            if rIndx<dIndx:
                R.append(rIndx+n)
            else:
                D.append(dIndx+n)
        return "Radiant" if R else "Dire"
        