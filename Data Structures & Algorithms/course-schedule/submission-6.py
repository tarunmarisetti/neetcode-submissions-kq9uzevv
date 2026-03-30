class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # tc O(noOfCourses + noofPrerequisites)

        # adjLst
        adjLst={}
        inDegree=[0]*numCourses
        for course, prerequisite in prerequisites:
            if prerequisite not in adjLst:
                adjLst[prerequisite]=[]
            adjLst[prerequisite].append(course)
            inDegree[course]+=1
        # print(adjLst)
        # print(inDegree)
        
        q=deque([i for i,course in enumerate(inDegree) if course==0])

        # print(q)
        while q:
            prerequisite=q.popleft()
            for course in adjLst.get(prerequisite,[]):
                inDegree[course]-=1
                if inDegree[course]==0:
                    q.append(course)
        return sum(inDegree)==0
        

        

        