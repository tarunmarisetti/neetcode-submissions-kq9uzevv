class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=[float('inf'),[0,0]]
        t_counter=Counter(t)
        need=len(t_counter)
        have=0
        window_counter=defaultdict(int)
        left=0
        for right in range(len(s)):
            window_counter[s[right]]+=1
            if s[right] in t_counter and window_counter[s[right]]==t_counter[s[right]]:
                have+=1
            while need==have:
                if right-left+1<res[0]:
                    res=[right-left+1,[left,right]]
                window_counter[s[left]]-=1
                if s[left] in t_counter and window_counter[s[left]]<t_counter[s[left]]:
                    have-=1
                left+=1
        left,right=res[1]
        return s[left:right+1] if res[0]!=float('inf') else ''

                

            

        