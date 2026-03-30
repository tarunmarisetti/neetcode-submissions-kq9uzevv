class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for ast in asteroids:
            alive=True
            while stk and stk[-1]>0 and ast<0:
                if stk[-1]<-ast:
                    stk.pop()
                    continue
                elif stk[-1]==-ast:
                    stk.pop()
                alive=False
                break
            if alive:
                stk.append(ast)
        return stk
        