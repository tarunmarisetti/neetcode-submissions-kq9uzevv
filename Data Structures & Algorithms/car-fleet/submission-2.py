class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine=[]
        for pos, speed in zip(position,speed):
            combine.append((pos,speed))
        combine.sort(key= lambda x:x[0],reverse=True)
        stk=[]
        for pos,speed in combine:
            currTime=(target-pos)/speed
            if stk and stk[-1]>=currTime:
                continue
            stk.append(currTime)
        return len(stk)
        