def solution(winners, coins):
    coins.sort(reverse=True)
    moneybox = coins[0:winners:]
    coins = coins[winners:]
    while coins != []:
        moneybox[-1] += coins.pop(0)
        moneybox.sort(reverse=True)
    prize = moneybox[0]
    for i in moneybox:
        if i != prize:
            return print(False)
    print(True)


if __name__ == "__main__":
    winners = int(input())
    number_of_coin = input()
    coins = [int(i) for i in input().split()]
    solution(winners, coins)
