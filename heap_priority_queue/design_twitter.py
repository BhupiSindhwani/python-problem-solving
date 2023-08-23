"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and
is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user themselves.
Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user followerId started unfollowing the user with ID followeeId.
"""
import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.next_activity_time = -1
        self.user_follow_map = defaultdict(set)
        self.user_tweets_map = defaultdict(list)
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.next_activity_time, tweetId))
        self.next_activity_time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_follow_map[userId].add(userId)
        followees = self.user_follow_map[userId]
        user_time_line = []
        result = []

        for followee in followees:
            idx = len(self.user_tweets_map[followee]) - 1
            if idx >= 0:
                activity_time, tweet_id = self.user_tweets_map[followee][idx]
                user_time_line.append([activity_time, tweet_id, followee, idx - 1])
        heapq.heapify(user_time_line)

        while user_time_line and len(result) < 10:
            activity_time, tweet_id, followee, idx = heapq.heappop(user_time_line)
            result.append(tweet_id)
            if idx >= 0:
                activity_time, tweet_id = self.user_tweets_map[followee][idx]
                heapq.heappush(user_time_line, [activity_time, tweet_id, followee, idx - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow_map[followerId]:
            self.user_follow_map[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))

    twitter.follow(1, 3)
    twitter.follow(1, 2)
    twitter.postTweet(3, 7)
    twitter.postTweet(3, 8)
    twitter.postTweet(3, 9)
    twitter.postTweet(3, 10)
    twitter.postTweet(3, 11)
    twitter.postTweet(2, 12)
    twitter.postTweet(1, 13)
    twitter.postTweet(2, 19)
    twitter.postTweet(1, 29)
    twitter.postTweet(3, 109)
    print(twitter.getNewsFeed(1))
