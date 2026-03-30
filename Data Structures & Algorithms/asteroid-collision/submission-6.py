class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for asteroid in asteroids:
            alive=True
            while stk and stk[-1]>0 and asteroid<0:
                if stk[-1]<-asteroid:
                    stk.pop()
                    continue #after poping we use continue to check the stk
                elif stk[-1]==-asteroid:
                    stk.pop()
                alive=False
                break #after exploding both we need to break as there is no asteroid
            if alive:
                stk.append(asteroid)
        return stk
        