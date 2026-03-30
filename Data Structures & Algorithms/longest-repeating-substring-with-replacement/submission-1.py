class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count=max_freq=0
        left=0
        window_counter=defaultdict(int)
        for right in range(len(s)):
            window_counter[s[right]]+=1
            max_freq=max(max_freq,window_counter[s[right]])
            while ((right-left+1)-max_freq)>k:
                window_counter[s[left]]-=1
                left+=1
            max_count=max(max_count, right-left+1)
        return max_count

        