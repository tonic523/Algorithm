import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
in_o = input().rstrip().split()
post_o = input().rstrip().split()

def solve(in_o, post_o):
    if len(post_o) == 0:
        return ""
    v = post_o.pop()
    if len(post_o) == 0:
        return v
    r_in = deque()
    r_post = deque()
    while in_o:
        temp = in_o.pop()
        if temp == v:
            break
        r_in.appendleft(temp)
        r_post.appendleft(post_o.pop())
    return v + " " + solve(in_o, post_o) + " " + solve(r_in, r_post) + " "
solve(in_o, post_o)