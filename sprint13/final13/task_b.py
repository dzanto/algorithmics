# 37655560
import sys
sys.setrecursionlimit(10000)


def search(arr, searched_element, left, right):
    if right == left and arr[left] == searched_element:
        return left
    if left < right:
        mid = (left + right) // 2
        if searched_element == arr[mid]:
            return mid
        elif searched_element == arr[left]:
            return left
        elif searched_element == arr[right]:
            return right
        else:
            if search(arr, searched_element, left=left, right=mid - 1) != -1:
                return search(arr, searched_element, left=left, right=mid - 1)
            else:
                return search(arr, searched_element, left=mid + 1, right=right)
    else:
        return -1


if __name__ == "__main__":
    length = input()
    k = int(input())
    arr = list(map(int, input().split()))
    print(search(arr, k, 0, len(arr)-1))
