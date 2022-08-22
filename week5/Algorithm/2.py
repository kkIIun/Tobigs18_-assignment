import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def solve():
    n, k = map(int, input().split())
    dp = [[0 if i != 0 else 1 for i in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cnt = int(input())
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - cnt]

    print(dp[n][k])


if __name__ == "__main__":
    solve()
