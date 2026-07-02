class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix=strs[0]
        for string in strs[1:]:
            i=0
            while i<min(len(string), len(commonPrefix)) and string[i]==commonPrefix[i]:
                i+=1
            commonPrefix=string[:i]
        return commonPrefix
        