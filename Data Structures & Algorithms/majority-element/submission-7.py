class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap={}
        for num in nums:
            if num not in freqMap:
                freqMap[num]=0
            freqMap[num]+=1 
        majEle=majFreq=0
        for key, val in freqMap.items():
            if val>majFreq:
                majEle=key
                majFreq=val
        return majEle
            
        