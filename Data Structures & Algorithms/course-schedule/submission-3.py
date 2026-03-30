class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        degree=[0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            degree[course]+=1
        
        course_completed=0
        q=deque()
        for i in range(numCourses):
            if degree[i]==0:
                q.append(i)
        while q:
            course=q.popleft()
            course_completed+=1
            for neighbour in graph[course]:
                degree[neighbour]-=1
                if degree[neighbour]==0:
                    q.append(neighbour)
        return course_completed==numCourses
        
        
        