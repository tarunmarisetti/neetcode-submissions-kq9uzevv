class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReqGrid=[[False]*numCourses for _ in range(numCourses)]
        adj_lst=defaultdict(list)
        inDegree=[0]*numCourses
        for preq, course in prerequisites:
            adj_lst[preq].append(course)
            inDegree[course]+=1
        
        q=deque([i for i, prereqCount in enumerate(inDegree) if prereqCount==0])

        while q:
            preReqCourse=q.popleft()
            for course in adj_lst[preReqCourse]:
                preReqGrid[preReqCourse][course]=True

                for i in range(numCourses):
                    if preReqGrid[i][preReqCourse]==True:
                        preReqGrid[i][course]=True
                inDegree[course]-=1
                if inDegree[course]==0:
                    q.append(course)
        
        return [preReqGrid[preq][course] for preq, course in queries]        