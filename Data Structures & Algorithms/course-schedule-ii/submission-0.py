class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        degree=[0]*numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            degree[course]+=1
        
        completed_courses=0
        in_order=[]
        q=deque()
        for i in range(numCourses):
            if degree[i]==0:
                q.append(i)
        while q:
            course=q.popleft()
            completed_courses+=1
            in_order.append(course)
            for neighbour in graph[course]:
                degree[neighbour]-=1
                if degree[neighbour]==0:
                    q.append(neighbour)
        return in_order if completed_courses==numCourses else []

        