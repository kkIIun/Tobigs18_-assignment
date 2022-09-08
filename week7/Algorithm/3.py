import sys, math
import itertools

input = sys.stdin.readline
INF = sys.maxsize


def SecValue(arr):
    sortedArr = sorted(list(itertools.chain.from_iterable(arr)))
    return sortedArr[-2]


def solve(Map):
    if len(Map) == 1:
        return Map[0][0]

    div = len(Map) // 2
    new_Map = [[0 for _ in range(div)] for _ in range(div)]
    for i in range(div):
        for j in range(div):
            new_Map[i][j] = SecValue(
                [Map[k][j * 2 : (j + 1) * 2] for k in range(i * 2, (i + 1) * 2)]
            )
    return solve(new_Map)


if __name__ == "__main__":
    n = int(input())
    Map = [list(map(int, input().split())) for _ in range(n)]
    print(solve(Map))
