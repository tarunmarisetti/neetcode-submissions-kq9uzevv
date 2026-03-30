class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word }
        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            min_len=min(len(s1),len(s2))
            if len(s1)>len(s2) and s1[:min_len]==s2[:min_len]:
                return ""
            for j in range(min_len):
                if s1[j]!=s2[j]:
                    adj[s1[j]].add(s2[j])
                    break
        print(adj)
        indegree={ch:0 for ch in adj}
        for ch in adj:
            for neigh in adj[ch]:
                indegree[neigh]+=1
        print(indegree)
        queue=deque(ch for ch in indegree if indegree[ch]==0)
        order=[]
        while queue:
            curr_char=queue.popleft()
            order.append(curr_char)
            for neigh in adj[curr_char]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        if len(order)<len(indegree):
            return ""
        return "".join(order)
