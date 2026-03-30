class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNeighbours(code):
            neighbourCodes=[]
            for i in range(4):
                num=int(code[i])
                for j in [1, -1]:
                    newNum=(num+j)%10
                    newCode=code[:i]+str(newNum)+code[i+1:]
                    neighbourCodes.append(newCode)
            return neighbourCodes

        deadends=set(deadends)
        start='0000'
        if start in deadends:
            return -1
        steps=0
        visited=set()
        q=deque([(start,steps)])
        while q:
            code,steps=q.popleft()
            if code==target:
                return steps
            neighborCodes=getNeighbours(code)
            for nCode in neighborCodes:
                if nCode not in deadends and nCode not in visited:
                    q.append((nCode, steps+1))
                    visited.add(nCode)
        return -1            
        