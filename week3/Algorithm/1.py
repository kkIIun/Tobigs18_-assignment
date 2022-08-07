from re import A
import sys, math
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

overlap = ["0"]


def is_prime(num):
    if num == 0 or num == 1:
        return 0

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def recFunc(num, arr, curidx):
    count = 0
    
    if num:
        count = is_prime(int(num))

    for i in range(len(arr)):
        new_num = num + arr[i]
        if i not in curidx and new_num not in overlap:
            overlap.append(new_num)
            curidx.append(i)
            count += recFunc(new_num, arr, curidx)
            curidx.remove(i)

    return count


def solve():
    curidx = []
    print(recFunc("", list(input().rstrip()), curidx))


if __name__ == "__main__":
    solve()
