def relative_sorting(numbers_for_sort, sample):
    work_dict = {i: i for i in sample}
    print(work_dict.values())


if __name__ == '__main__':
    length_numbers_for_sort = input()
    numbers_for_sort = [int(i) for i in input().split()]
    length_sample = input()
    sample = [int(i) for i in input().split()]
    relative_sorting(numbers_for_sort, sample)
