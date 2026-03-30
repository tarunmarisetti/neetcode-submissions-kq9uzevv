class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        tCounter=Counter(t)
        windowCounter=defaultdict(int)
        res=[float('inf'),0,0]
        need=len(tCounter)
        have=0
        for right in range(len(s)):
            windowCounter[s[right]]+=1
            if s[right] in tCounter and windowCounter[s[right]]==tCounter[s[right]]:
                have+=1
            while need==have:
                if right-left+1<res[0]:
                    res=[right-left+1, left, right]
                windowCounter[s[left]]-=1
                if s[left] in tCounter and windowCounter[s[left]]<tCounter[s[left]]:
                    have-=1
                left+=1
        resLen, l, r=res
        return s[l:r+1] if resLen!=float('inf') else ""


        