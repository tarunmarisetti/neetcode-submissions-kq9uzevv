class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        maxFreq=maxCount=0
        windowFreq=defaultdict(int)
        for right in range(len(s)):
            windowFreq[s[right]]+=1
            maxFreq=max(maxFreq, windowFreq[s[right]])
            while (right-left+1)-maxFreq>k:
                windowFreq[s[left]]-=1
                left+=1
            maxCount=max(maxCount, right-left+1)
        return maxCount

            

        