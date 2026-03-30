class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs=[(pos,speedd) for pos,speedd in zip(position,speed)]
        pairs.sort(reverse=True)
        stk=[]
        for position,speed in pairs:
            remain_dist=target-position
            time_to_reach=remain_dist/speed
            stk.append(time_to_reach)
            # if we have two cars and top_car time_to_reach is less than the car infront of it we will remove the top_car
            while len(stk)>=2 and stk[-1]<=stk[-2]:
                stk.pop()
        return len(stk)
