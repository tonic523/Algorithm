import sys

input = sys.stdin.readline

def hash_function(string):
    MAX = 1234567891
    ASCII_A = ord('a')
    hashcode = 0
    for i, c in enumerate(string):
        hashcode += (ord(c) - ASCII_A + 1) * (31 ** i)
    return hashcode % MAX

L = int(input())
string = input().rstrip()

print(hash_function(string))