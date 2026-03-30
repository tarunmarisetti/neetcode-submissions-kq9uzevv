class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        window_freq=defaultdict(int)
        max_count=0
        for right in range(len(s)):
            window_freq[s[right]]+=1
            while window_freq[s[right]]>1:
                if window_freq[s[left]]==1:
                    del window_freq[s[left]]
                else:
                    window_freq[s[left]]-=1
                left+=1
            max_count=max(max_count,right-left+1)
        return max_count  
        