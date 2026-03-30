class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.followMap=defaultdict(set)
        self.count=0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        max_heap=[]
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                recentTweetIndex=len(self.tweets[followeeId])-1
                count,recentTweetId=self.tweets[followeeId][recentTweetIndex]
                heapq.heappush(max_heap,(count,recentTweetId, followeeId, recentTweetIndex-1))

        while max_heap and len(res)<10:
            count, tweetId, followeeId, recentTweetIndex=heapq.heappop(max_heap)
            res.append(tweetId)
            if recentTweetIndex>=0:
                nextCount, nextTweetId=self.tweets[followeeId][recentTweetIndex]
                heapq.heappush(max_heap,(nextCount, nextTweetId, followeeId, recentTweetIndex-1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
