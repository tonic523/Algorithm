import sys

input = sys.stdin.readline

N = int(input())

friendships = []

for i in range(N):
    Y_N = list(input().rstrip())
    friendship = set()
    for j in range(N):
        if Y_N[j] == "Y":
            friendship.add(j)
    friendships.append(friendship)

max_friend_count = 0

for i in range(N):
    friend = set(friendships[i])
    for f in friendships[i]:
        friend.update(friendships[f])
    if i in friend:
        friend.remove(i)
    max_friend_count = max(max_friend_count, len(friend))

print(max_friend_count)
