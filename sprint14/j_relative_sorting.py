def relative_sorting(numbers_for_sort, sample):
    work_dict = {i: 0 for i in sample}
    set_sample = set(sample)
    sorted_arr = []
    not_sort = []
    for i in numbers_for_sort:
        if i in set_sample:
            work_dict[i] += 1
        else:
            not_sort.append(i)
    not_sort.sort()
    for a, b in work_dict.items():
        for cnt in range(b):
            sorted_arr.append(a)
    sorted_arr.extend(not_sort)
    return sorted_arr


if __name__ == '__main__':
    length_numbers_for_sort = int(input())
    if length_numbers_for_sort == 0:
        print('')
    else:
        numbers_for_sort = [int(i) for i in input().split()]
        length_sample = int(input())
        if length_sample == 0:
            sorted_arr = sorted(numbers_for_sort)
        else:
            sample = [int(i) for i in input().split()]
            sorted_arr = relative_sorting(numbers_for_sort, sample)
        print(' '.join(map(str, sorted_arr)))
