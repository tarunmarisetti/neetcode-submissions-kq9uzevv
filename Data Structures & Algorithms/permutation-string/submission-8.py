class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len,s2_len=len(s1), len(s2)
        if s1_len > s2_len:
            return False
        left=0
        s1_freq=Counter(s1)
        window_freq=Counter()
        for right in range(s2_len):
            window_freq[s2[right]]+=1
            if right+1>s1_len:
                old_char=s2[left]
                if window_freq[old_char]==1:
                    del window_freq[old_char]
                else:
                    window_freq[old_char]-=1
                left+=1
            print(window_freq)
            if window_freq==s1_freq:
                return True
        return False
        