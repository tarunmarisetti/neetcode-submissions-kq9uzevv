class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,nodeA, nodeB):
        rootA,rootB=self.find(nodeA), self.find(nodeB)
        if rootA==rootB:
            return
        if self.rank[rootA]>self.rank[rootB]:
            self.parent[rootB]=rootA
        elif self.rank[rootA]<self.rank[rootB]:
            self.parent[rootA]=rootB
        else:
            self.parent[rootB]=rootA
            self.rank[rootA]+=1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu=DSU(len(accounts))
        emailToAcc=defaultdict(list) #email-->accountIndx
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    dsu.union(emailToAcc[email],i)
                else:
                    emailToAcc[email]=i
        
        indxToEmail=defaultdict(list)
        for email, indx in emailToAcc.items():
            parent=dsu.find(indx)
            indxToEmail[parent].append(email)
        
        # print(indxToEmail)

        res=[]
        for indx, emails in indxToEmail.items():
            # print(sorted(emails))
            res.append([accounts[indx][0]]+sorted(emails))
        return res



        