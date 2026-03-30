class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix=strs[0]
        for word in strs[1:]:
            i=0
            while i<min(len(common_prefix),len(word)) and word[i]==common_prefix[i]:
                i+=1
            common_prefix=word[:i]
        return common_prefix
                


        