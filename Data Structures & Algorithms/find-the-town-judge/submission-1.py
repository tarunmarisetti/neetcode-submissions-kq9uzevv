class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town_judge=trust[0][1]
        for a,b in trust[1:]:
            if b!=town_judge:
                return -1
        return town_judge
        