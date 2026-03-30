class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        reversed_x=0
        while x:
            rem=x%10
            reversed_x=reversed_x*10+rem
            if reversed_x>2**31-1:
                return 0
            x=x//10
        return sign*reversed_x
        

        