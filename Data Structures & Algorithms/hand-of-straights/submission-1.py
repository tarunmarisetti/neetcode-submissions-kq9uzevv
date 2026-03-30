class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        freq=Counter(hand)
        hand.sort()
        for num in hand:
            if freq[num]:
                for i in range(num, num+groupSize):
                    if not freq[i]:
                        return False
                    freq[i]-=1
        return True
                    