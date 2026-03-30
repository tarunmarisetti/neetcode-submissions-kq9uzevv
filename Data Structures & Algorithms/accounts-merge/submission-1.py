class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x]) #path compression
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
        emailToIndx=defaultdict(int)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIndx:
                    dsu.union(emailToIndx[email],i)
                else:
                    emailToIndx[email]=i

        indexToEmail=defaultdict(list)
        for email, indx in emailToIndx.items():
            parent=dsu.find(indx)
            indexToEmail[parent].append(email)
        
        res=[]
        for indx, emails in indexToEmail.items():
            sortedEmails=sorted(emails)
            res.append([accounts[indx][0]]+sortedEmails)
        return res





        