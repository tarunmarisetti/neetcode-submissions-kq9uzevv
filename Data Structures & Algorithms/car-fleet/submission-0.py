class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(pos,s) for pos, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stk=[]
        for pos,speed in pairs:
            stk.append((target-pos)/speed)
            if len(stk)>=2 and stk[-1]<=stk[-2]:
                stk.pop()
        return len(stk)

        