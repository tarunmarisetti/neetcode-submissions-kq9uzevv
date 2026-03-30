class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for asteroid in asteroids:
            isAlive=True
            while stk and stk[-1]>0 and asteroid<0:
                if stk[-1]-abs(asteroid)==0:
                    stk.pop()
                    isAlive=False
                    break
                elif stk[-1]<abs(asteroid):
                    stk.pop()
                else:
                    isAlive=False
                    break

            if isAlive:
                stk.append(asteroid)
        return stk

        