class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # using dfs
        # adj_lst
        adj_lst={}
        for preq, course in prerequisites:
            if course not in adj_lst:
                adj_lst[course]=[]
            adj_lst[course].append(preq)
        
        def dfs(source, dest, visited):
            if source==dest:
                return True
            for neigh in adj_lst.get(dest,[]):
                if neigh in visited:
                    continue
                visited.add(neigh)
                if dfs(source, neigh, visited):
                    return True
            return False

        res=[]
        for source, dest in queries:
            res.append(dfs(source, dest, set()))
        return res

       