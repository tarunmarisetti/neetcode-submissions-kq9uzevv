class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        longest_len=0
        freq_count=Counter()
        for right in range(len(s)):
            freq_count[s[right]]+=1
            max_freq=max(max_freq, freq_count[s[right]])
            while (right-left+1)-max_freq>k:
                print((right-left+1)-max_freq)
                freq_count[s[left]]-=1
                left+=1
            longest_len=max(longest_len,right-left+1) 
        return longest_len

        