class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = collections.defaultdict(set)
        self.twitts = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.twitts[userId].insert(0, (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = [self.twitts[followeeId] for followeeId in self.followers[userId]] + [self.twitts[userId]]

        def merge(arr1, arr2):
            i = j = 0

            result = []

            while len(result) < 10 and i < len(arr1) and j < len(arr2):
                if arr1[i][0] > arr2[j][0]:
                    result.append((arr1[i][0], arr1[i][1]))
                    i += 1
                else:
                    result.append((arr2[j][0], arr2[j][1]))
                    j += 1

            while len(result) < 10 and i < len(arr1):
                result.append((arr1[i][0], arr1[i][1]))
                i += 1

            while len(result) < 10 and j < len(arr2):
                result.append((arr2[j][0], arr2[j][1]))
                j += 1

            return result

        while len(feed) > 1: feed.append(merge(feed.pop(), feed.pop()))

        return [tweetId for time, tweetId in feed[0][:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followeeId in self.followers[followerId]: return None
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followeeId not in self.followers[followerId]: return None
        self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
