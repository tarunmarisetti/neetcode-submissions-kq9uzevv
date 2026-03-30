class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj_lst=defaultdict(list)
        neighNodeCount=[0]*n
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
            neighNodeCount[u]+=1
            neighNodeCount[v]+=1
        # print(adj_lst)
        # print(neighNodeCount)

        leaves=deque([i for i, nodeCount in enumerate(neighNodeCount) if nodeCount==1])

        while leaves:
            """
            here for a tree the max nodes that can be root are 2
            case1 1 if the no of nodes in the longest path of the tree is odd
            case 2 if no of nodes in the longest path is even"""
            if n<=2:
                return list(leaves)
            # here we should go layer by layer so thats why we using for loop
            for i in range(len(leaves)):
                currleave=leaves.popleft()
                n-=1
                for neigh in adj_lst[currleave]:
                    neighNodeCount[neigh]-=1
                    if neighNodeCount[neigh]==1:
                        leaves.append(neigh)

        
        