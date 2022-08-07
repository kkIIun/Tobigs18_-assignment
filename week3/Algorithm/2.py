import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def recFunc(num, arr, curidx, m):
    Max = 0
    if len(curidx) == 3:
        return num

    for i in range(len(arr)):
        new_num = num + arr[i]
        if i not in curidx and new_num <= m:
            curidx.append(i)
            Max = max(Max, recFunc(new_num, arr, curidx, m))
            curidx.remove(i)

    return Max


def solve():
    curidx = []
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    print(recFunc(0, arr, curidx, m))


if __name__ == "__main__":
    solve()
