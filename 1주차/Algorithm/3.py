import sys
from collections import deque
import math

input = sys.stdin.readline
INF = sys.maxsize


def solve():
    U, D, H = map(int, sys.stdin.readline().split(" "))
    print(math.ceil((H - U) / (U - D) * 1.0) + 1)


if __name__ == "__main__":
    solve()
