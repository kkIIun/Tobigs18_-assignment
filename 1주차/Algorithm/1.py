import sys
import queue

move = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


def solve():
    n = int(sys.stdin.readline())
    curr = [1, 1]

    char = sys.stdin.readline().rstrip().split(" ")
    for c in char:
        if n >= curr[0] + move[c][0] > 0 and n >= curr[1] + move[c][1] > 0:
            curr[0] += move[c][0]
            curr[1] += move[c][1]
    print(curr[0], curr[1])


if __name__ == "__main__":
    solve()
