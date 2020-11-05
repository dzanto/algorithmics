def flowerbed(flowerbeds):
    flowebeds.sort(key=lambda x: x[0])
    # print(flowebeds)
    start = flowebeds[0][0]
    end = flowebeds[0][1]
    for i in flowebeds:
        if i[0] > end:
            print(start, end)
            start = i[0]
        if end < i[1]:
            end = i[1]
    print(start, end)


if __name__ == '__main__':
    gardener = int(input())
    flowebeds = []
    for i in range(gardener):
        array = [int(i) for i in input().split()]
        flowebeds.append(array)
    # print(flowebeds)
    flowerbed(flowebeds)
