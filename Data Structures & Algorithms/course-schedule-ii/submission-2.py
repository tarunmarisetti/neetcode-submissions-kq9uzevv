class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahns algorithm
        adj_lst=defaultdict(list)
        preRequisiteCount=[0]*numCourses
        for course, prereq in prerequisites:
            adj_lst[prereq].append(course)
            preRequisiteCount[course]+=1
        # print(adj_lst,preRequisiteCount)

        q=deque([i for i,count in enumerate(preRequisiteCount) if count==0])

        order=[]
        completedCourses=0
        while q:
            currCourse=q.popleft()
            order.append(currCourse)
            completedCourses+=1
            for course in adj_lst[currCourse]:
                preRequisiteCount[course]-=1
                if preRequisiteCount[course]==0:
                    q.append(course)
        return order  if completedCourses==numCourses else []  
        