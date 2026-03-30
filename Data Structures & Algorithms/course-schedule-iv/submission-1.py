class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # using topilogicalsort
        # O(v+E)
        inDegree=[0]*numCourses
        adj_lst=defaultdict(list)
        for preq, course in prerequisites:
            adj_lst[preq].append(course)
            inDegree[course]+=1
        # print(adj_lst)

        finalPreq=[set() for _ in range(numCourses)]

        q=deque([course for course, count in enumerate(inDegree) if count==0 ])

        while q:
            preq=q.popleft()
            for course in adj_lst[preq]:
                finalPreq[course].add(preq)
                finalPreq[course].update(finalPreq[preq])  #updating the set (optimal way)
                inDegree[course]-=1
                if inDegree[course]==0:
                    q.append(course)
        # print(finalPreq)
        res=[]
        for preq, course in queries:
            res.append(preq in finalPreq[course])
        return res               

        
        