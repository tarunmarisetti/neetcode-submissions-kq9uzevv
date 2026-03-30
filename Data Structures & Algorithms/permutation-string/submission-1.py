class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_freq=Counter(s1)
        wind_freq=Counter(s2[:len(s1)])
        for i in range(len(s1),len(s2)):
            if wind_freq==s1_freq:
                return True
            oldChar=s2[i-len(s1)]
            newChar=s2[i]
            if wind_freq[oldChar]==1:
                del wind_freq[oldChar]
            else:
                wind_freq[oldChar]-=1
            wind_freq[newChar]+=1
        return wind_freq==s1_freq

        