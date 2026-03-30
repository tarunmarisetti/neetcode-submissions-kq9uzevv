class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        start='0000'
        if start in deadends:
            return -1
               
        turn=0
        q=deque([(start,turn)])
        visitedCombinations=set()
        visitedCombinations.add(start)

        while q:
            code,turn=q.popleft()
            if code==target:
                return turn
            for i in range(4):
                currNum=int(code[i])
                for j in [1,-1]:
                    newNum=(currNum+j)%10
                    newCode=code[:i]+str(newNum)+code[i+1:]
                    if newCode not in deadends and newCode not in visitedCombinations:
                        q.append((newCode, turn+1))
                        visitedCombinations.add(newCode)
        return -1



        