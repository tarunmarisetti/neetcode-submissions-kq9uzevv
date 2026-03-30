class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix=strs[0]
        for word in strs[1:]:
            common_word=""
            i=0
            while i<len(common_prefix) and i<len(word) and word[i]==common_prefix[i]:
                common_word+=word[i]
                i+=1
            common_prefix=common_word
        return common_prefix
                


        