class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.user_post = defaultdict(list)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1 
        self.user_post[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = [userId] + list(self.follow_map[userId])

        for user in users:
            for post in self.user_post[user]:
                heapq.heappush(heap,post)
            while len(heap) > 10:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(10) if heap][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
