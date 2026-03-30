class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        for i in range(len(trust)-1):
            if trust[i][1]!=trust[i+1][1]:
                return -1
        return trust[0][1]

        