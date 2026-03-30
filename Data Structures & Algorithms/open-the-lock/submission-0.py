class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbours(s):
            neighbours=[]
            for i in range(4):
                num=int(s[i])
                for step in [1,-1]:
                    new_num=(num+step)%10
                    new_s=s[:i]+str(new_num)+s[i+1:]
                    neighbours.append(new_s)
            return neighbours

        deadends=set(deadends)
        start='0000'
        if start in deadends:
            return -1
        steps=0
        visited=set()
        queue=deque([(start,steps)])

        while queue:
            combination,steps=queue.popleft()
            if combination==target:
                return steps
            neighbours=get_neighbours(combination)
            for neighbour in neighbours:
                if neighbour not in deadends and neighbour not in visited:
                    queue.append((neighbour,steps+1))
                    visited.add(neighbour)
        return -1

        