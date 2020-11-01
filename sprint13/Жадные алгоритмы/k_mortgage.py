def solution(houses_and_budget, coasts):
    houses = houses_and_budget[0]
    budget = houses_and_budget[1]
    coasts.sort(reverse=True)
    new_houses = 0
    for i in range(houses):
        if coasts == []:
            return new_houses
        if budget < coasts[-1]:
            return new_houses
        budget -= coasts.pop(-1)
        new_houses += 1
    return new_houses


if __name__ == '__main__':
    houses_and_budget = [int(i) for i in input().split()]
    coasts = [int(i) for i in input().split()]
    print(solution(houses_and_budget, coasts))