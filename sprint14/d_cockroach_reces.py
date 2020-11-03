def quicksort(first_race, second_race):
    lawbreackers = []
    for i in first_race:
        if i in second_race:
            lawbreackers.append(i)
    return lawbreackers



if __name__ == '__main__':
    n = input()
    m = input()
    first_race = [int(i) for i in input().split()]
    second_race = [int(i) for i in input().split()]
    rez = quicksort(first_race, second_race)
    print(' '.join(map(str, rez)))