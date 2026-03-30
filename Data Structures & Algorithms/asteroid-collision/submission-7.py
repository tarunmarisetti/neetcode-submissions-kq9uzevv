class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            is_alive=True
            while stack and stack[-1]>0 and asteroid<0:
                if stack[-1]<-asteroid:
                    stack.pop()
                    continue
                elif stack[-1]==-asteroid:
                    stack.pop()
                is_alive=False
                break
                
            if is_alive:
                stack.append(asteroid)
        return stack
        