import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
know_p = set(list(map(int, input().rstrip().split()))[1:])
party_li = []

for _ in range(M):
    party_li.append(set(list(map(int, input().rstrip().split()))[1:]))

def dfs(party_li):
    global know_p
    global no_lie_party
    for i, party in enumerate(party_li):
        for p in party:
            if p in know_p:
                know_p = know_p | party
                party_li.pop(i)
                dfs(party_li)
                break

dfs(party_li)

print(len(party_li))