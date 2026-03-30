from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map=defaultdict(list)
        for strng in strs:
            key=tuple(sorted(strng))
            str_map[key].append(strng)
        print(str_map)
        return list(str_map.values())
        