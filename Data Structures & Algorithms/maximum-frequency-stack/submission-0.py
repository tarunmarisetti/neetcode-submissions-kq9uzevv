class FreqStack:

    def __init__(self):
        self.max_freq=0
        self.freq_map=defaultdict(int)
        self.group=defaultdict(list)

    def push(self, val: int) -> None:
        self.freq_map[val]+=1
        self.group[self.freq_map[val]].append(val)
        self.max_freq=max(self.max_freq,self.freq_map[val])

    def pop(self) -> int:
        val=self.group[self.max_freq].pop()
        self.freq_map[val]-=1
        if not self.group[self.max_freq]:
            self.max_freq-=1
        return val


# max_freq=3
# freq_map{5:3,7:2,4:1}
# group1->[5,7,4]
# group2->[5,7]
# group3->[5]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()