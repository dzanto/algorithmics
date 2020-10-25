# 37678604
def photos(arr):
    count = 0
    if len(arr) == 1:
        return 0
    arr.sort(reverse=True)
    while (arr[0] > 0) and (arr[1] > 0):
        arr[0] -= 1
        arr[1] -= 1
        count += 1
        arr.sort(reverse=True)
    return count


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(photos(arr))
