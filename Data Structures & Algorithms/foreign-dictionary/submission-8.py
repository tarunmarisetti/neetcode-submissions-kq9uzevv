class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_lst={}
        for word in words:
            for char in word:
                adj_lst[char]=set()
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            word1_len=len(word1)
            word2_len=len(word2)
            min_len=min(word1_len,word2_len)
            if word1_len>word2_len and word1[:min_len]==word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j]!=word2[j]:
                    adj_lst[word1[j]].add(word2[j])
                    break
        
        indegree={char:0 for char in adj_lst}

        for char in adj_lst:
            for neighbor in adj_lst[char]:
                indegree[neighbor]+=1
        q=deque([char for char in indegree if indegree[char]==0])

        order=[]
        while q:
            char=q.popleft()
            order.append(char)
            for neighbor in adj_lst[char]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        if len(order)!=len(indegree):
            return ""
        return "".join(order)


        