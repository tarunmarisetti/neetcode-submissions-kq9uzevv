class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_lst={}
        for word in words:
            for char in word:
                adj_lst[char]=set()
        n=len(words)
        for i in range(n-1): 
            word1,word2=words[i], words[i+1]
            word1_len,word2_len=len(word1), len(word2)
            min_len=min(word1_len, word2_len)
            if len(word1)>len(word2) and word1[:min_len]==word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j]!=word2[j]:
                    adj_lst[word1[j]].add(word2[j])
                    break
        
        print(adj_lst)
        # in order 
        inDegree={key:0 for key in adj_lst.keys()}
        for char in adj_lst:
            for neighbor in adj_lst[char]:
                inDegree[neighbor]+=1
        print(inDegree)

        q=deque([char for char,value in inDegree.items() if value==0])

        order=[]
        while q:
            char=q.popleft()
            order.append(char)
            for neighbor in adj_lst[char]:
                inDegree[neighbor]-=1
                if inDegree[neighbor]==0:
                    q.append(neighbor)
       
        return "".join(order)  if len(order)==len(inDegree) else ""



                
        