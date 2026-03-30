class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found=set()
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
            for i,num in enumerate(triplet):
                if num==target[i]:
                    found.add(i)
        return len(found)==3
        