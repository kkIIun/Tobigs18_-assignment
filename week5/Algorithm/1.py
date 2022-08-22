import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def solve():
    height = list(map(int, input().split()))
    dp = [0 for _ in range(11)]
    dp[0] = 1

    for i in range(1, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for h in height:
        print(dp[h])


if __name__ == "__main__":
    solve()
