class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #tm O(numCourse + no of prerequisites)
        adjLst={}
        inDegree=[0]*numCourses
        for course, preReq in prerequisites:
            if preReq not in adjLst:
                adjLst[preReq]=[]
            adjLst[preReq].append(course)
            inDegree[course]+=1
        
        q=deque([i for i, course in enumerate(inDegree) if course==0])
        courseOrder=[]

        while q:
            prereq=q.popleft()
            courseOrder.append(prereq)
            for order in adjLst.get(prereq, []):
                inDegree[order]-=1
                if inDegree[order]==0:
                    q.append(order)
        return courseOrder if sum(inDegree)==0 else []
        