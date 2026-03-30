class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        R=deque()
        D=deque()

        for i,c in enumerate(senate):
            if c=='R':
                R.append(i)
            else:
                D.append(i)
        
        # print(R,D)
        while R and D:
            rIndx, dIndx=R.popleft(), D.popleft()
            if rIndx<dIndx:
                R.append(rIndx+n)
            else:
                D.append(dIndx+n)
        return "Radiant" if R else "Dire"

        