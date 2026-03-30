class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq_map={} #O(n)
        for num in hand:
            if num not in freq_map:
                freq_map[num]=0
            freq_map[num]+=1
        hand.sort() # nlogn
        for num in hand:
            if freq_map[num]>0:
                for j in range(num, num+groupSize):
                    if freq_map.get(j,0)<=0:
                        return False
                    freq_map[j]-=1
        return True
        