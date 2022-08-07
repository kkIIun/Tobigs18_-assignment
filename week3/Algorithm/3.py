import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def get_change_count(arr, row, col, answer1, answer2):
    question = [i[col - 8 : col] for i in arr[row - 8 : row]]

    result1, result2 = 0, 0
    for i in range(8):
        for j in range(8):
            if question[i][j] != answer1[i][j]:
                result1 += 1

            if question[i][j] != answer2[i][j]:
                result2 += 1

    return min(result1, result2)


def get_answer():
    answer1 = [[None for _ in range(8)] for _ in range(8)]
    answer2 = [[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 1:
                answer1[i][j] = "R"
                answer2[i][j] = "B"

            elif i % 2 == 1 and j % 2 == 0:
                answer1[i][j] = "R"
                answer2[i][j] = "B"

            elif i % 2 == 1 and j % 2 == 1:
                answer1[i][j] = "B"
                answer2[i][j] = "R"

            elif i % 2 == 0 and j % 2 == 0:
                answer1[i][j] = "B"
                answer2[i][j] = "R"

    return answer1, answer2


def solve():
    Min = INF
    m, n = map(int, input().split(" "))
    arr = [list(input().rstrip()) for _ in range(m)]

    answer1, answer2 = get_answer()

    for i in range(8, m + 1):
        for j in range(8, n + 1):
            Min = min(Min, get_change_count(arr, i, j, answer1, answer2))

    print(Min)


if __name__ == "__main__":
    solve()
