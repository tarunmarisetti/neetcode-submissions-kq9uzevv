class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter=Counter(s1)
        s1_len=len(s1)
        left=0
        windowCounter=defaultdict(int)
        for right in range(len(s2)):
            windowCounter[s2[right]]+=1
            if (right-left+1)>s1_len:
                if windowCounter[s2[left]]==1:
                    del windowCounter[s2[left]]
                else:
                    windowCounter[s2[left]]-=1
                left+=1
            if windowCounter==s1Counter:
                return True
        return False

        