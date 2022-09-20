from black import contains_fmt_on_at_column


def solve(coins, money):
    count = 0
    while coins:
        coin = coins.pop()
        count = money // coin
        money = money % coin
        print(money)
    print(count)


if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = [None] * n
    for i in range(n):
        coins[i] = int(input())
    solve(coins, m)