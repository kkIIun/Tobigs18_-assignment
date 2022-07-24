import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def solve():
    n, m = map(int, sys.stdin.readline().split(" "))
    sorted = []
    for _ in range(n):
        arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        arr.sort()
        sorted.append(arr[0])
    sorted.sort()
    print(sorted[-1])


if __name__ == "__main__":
    solve()
