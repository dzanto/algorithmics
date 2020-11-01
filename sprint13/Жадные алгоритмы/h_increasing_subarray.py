def increasing_subarray(digits):
    current_count = 0
    common_count = 0

    for i in range(1, len(digits)):
        if digits[i-1] >= digits[i]:
            if current_count > common_count:
                common_count = current_count
            current_count = 0
        else:
            current_count += 1
    if current_count > common_count:
        common_count = current_count
    return common_count + 1

if __name__ == "__main__":

    number_of_digit = int(input())
    digits = [int(i) for i in input().split()]
    print(increasing_subarray(digits))

