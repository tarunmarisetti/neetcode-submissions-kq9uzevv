class MedianFinder:

    def __init__(self):
        self.data=[]

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        n=len(self.data)
        self.data.sort()
        mid=n//2
        if n%2==0:
            return (self.data[mid]+self.data[mid-1])/2
        else:
            return self.data[mid]
        
        