class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        s1_len=len(s1)
        window_counter=defaultdict(int)
        for i in range(len(s2)):
            window_counter[s2[i]]+=1
            if i>=s1_len:
                firstChar=s2[i-s1_len]
                if window_counter[firstChar]==1:
                    del window_counter[firstChar]
                else:
                    window_counter[firstChar]-=1
            if window_counter==s1_counter:
                return True
        return False
            

        