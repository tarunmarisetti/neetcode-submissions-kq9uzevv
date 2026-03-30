class Solution:
    def hammingWeight(self, n: int) -> int:
        noOfOnes=bin(n).count('1')
        return noOfOnes