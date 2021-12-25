import math
import sys

input = sys.stdin.readline

A, B, V = map(int, input().rstrip().split())
print(math.ceil((V - A) / (A - B)) + 1)