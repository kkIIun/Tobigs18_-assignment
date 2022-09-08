import sys, math
import itertools

input = sys.stdin.readline
INF = sys.maxsize


def solve(Map, ans):
    flatten = list(itertools.chain.from_iterable(Map))
    if len(list(set(flatten))) == 1:
        ans[Map[0][0]] += 1
        return ans

    div = len(Map) // 3
    for i in range(3):
        for j in range(3):
            solve([Map[k][j * div : (j + 1) * div] for k in range(i * div, (i + 1) * div)], ans)

    return ans


if __name__ == "__main__":
    n = int(input())
    Map = [list(map(int, input().split())) for _ in range(n)]
    ans = {-1: 0, 0: 0, 1: 0}
    for value in solve(Map, ans).values():
        print(value)
