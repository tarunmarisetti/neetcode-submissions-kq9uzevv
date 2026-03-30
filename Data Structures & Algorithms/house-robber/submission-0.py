class Solution:
    def rob(self, nums: List[int]) -> int:
        # here basically we need two values rob1 and rob2
        # [rob1,rob2,n,n+1,n+2.......]
        rob1=rob2=0
        for house in nums:
            temp=max(rob1+house,rob2) # here we are getting max of robbing the present hourse means we can add rob1+present house or dont 
            # rob the present house meaning taking only rob2
            rob1=rob2
            rob2=temp # shifting rob1 and rob2 to next
        return rob2

        