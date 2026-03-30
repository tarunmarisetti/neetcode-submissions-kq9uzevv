class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_lst={}
        inDegree={}
        for word in words:
            for char in word:
                adj_lst[char]=set()
                inDegree[char]=0

        # build the adj_lst and the inDegree 
        for i in range(len(words)-1):
            w1, w2=words[i], words[i+1]
            w1Len, w2Len=len(w1), len(w2)
            minLen=min(w1Len, w2Len)
            if w1Len>w2Len and w1[:minLen]==w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj_lst[w1[j]]: 
                        adj_lst[w1[j]].add(w2[j])
                        inDegree[w2[j]]+=1
                    break
        print(adj_lst)
        print(inDegree)

        q=deque([char for char, value in inDegree.items() if value==0])

        res=[]    
        while q:
            currChar=q.popleft()
            res.append(currChar)

            for neigh in adj_lst[currChar]:
                inDegree[neigh]-=1
                if inDegree[neigh]==0:
                    q.append(neigh)
        if len(res)!=len(inDegree):
            return ""
        return "".join(res)

            

        