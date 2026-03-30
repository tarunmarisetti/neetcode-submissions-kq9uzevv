class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for asteroid in asteroids:
            isAlive=True
            while stk and stk[-1]>0 and asteroid<0:
                if stk[-1]<-asteroid:
                    stk.pop()
                elif stk[-1]==-asteroid:
                    stk.pop()
                    isAlive=False
                    break
                elif stk[-1]>asteroid:
                    isAlive=False
                    break
            
            if isAlive:
                stk.append(asteroid)
        return stk