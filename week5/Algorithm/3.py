import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def solve():
    n = int(input())
    dp = [1 for _ in range(n + 1)]
    dp[1] = 0

    for i in range(2, n + 1):
        Min = dp[i - 1]

        if i % 2 == 0:
            Min = min(Min, dp[i // 2])
        if i % 3 == 0:
            Min = min(Min, dp[i // 3])

        dp[i] += Min
    print(dp[n])


if __name__ == "__main__":
    solve()
