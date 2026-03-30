class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter=Counter(t)
        window_counter=Counter()
        res=[float('inf'),0,0] #res=[min_len, left,right]
        req,have=len(t_counter),0
        left=0
        for right in range(len(s)):
            window_counter[s[right]]+=1
            if s[right] in t_counter and window_counter[s[right]]==t_counter[s[right]]:
                have+=1
            while req==have:
                if right-left+1 <res[0]:
                    res=[right-left+1,left,right]
                window_counter[s[left]]-=1
                if s[left] in t_counter and window_counter[s[left]]<t_counter[s[left]]:
                    have-=1
                left+=1
        min_len,left,right=res
        return s[left:right+1] if min_len != float('inf') else ""
        