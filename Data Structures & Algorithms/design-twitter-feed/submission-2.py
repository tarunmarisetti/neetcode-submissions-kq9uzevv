class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.follow_map=defaultdict(set)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap=[]
        res=[]
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweets:
                recent_tweet_index_of_followeeId=len(self.tweets[followeeId])-1
                count,recent_tweetId=self.tweets[followeeId][recent_tweet_index_of_followeeId]
                min_heap.append((count,recent_tweetId,followeeId,recent_tweet_index_of_followeeId-1))
        heapq.heapify(min_heap)

        while min_heap and len(res)<10:
            count,recent_tweetId,followeeId,recent_tweet_index=heapq.heappop(min_heap)
            res.append(recent_tweetId)
            if recent_tweet_index>=0:
                next_count,next_tweetId=self.tweets[followeeId][recent_tweet_index]
                heapq.heappush(min_heap,(next_count,next_tweetId,followeeId,recent_tweet_index-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
