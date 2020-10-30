sequence = list(map(int, input()))
buttons = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}
list_x = []


# for num1 in sequence:
#     for letter1 in buttons[num1]:
#         for num2 in sequence:
#             if num1 == num2:
#                 continue
#             for letter2 in buttons[num2]:
#                 list_x.append(letter1+letter2)
#     # break
# print(' '.join(list_x))

# for i in sequence:
#     for
# len_sequence = len(sequence)
# for i_s in range(len_sequence):
#     len_button = len(buttons[sequence[i_s]])
#     for i_b in range(len_button):
#         list_x.append(buttons[sequence[i_s]][i_b])
#     print(list_x)
#     print(' '.join(list_x))


def get_letter(button_num, letter_num):
    letters = buttons[button_num]
    letter = letters[letter_num]
    return letter


print(get_letter(2, 0))

count_seq = 0
while count_seq < len(sequence):
    for letter1 in buttons[sequence[0]]:
        button_num = sequence[count_seq]
        world1 = letter1 + get_letter(sequence[button_num], letter_num)

        for letter2 in buttons
        world1 = letter + get_letter(sequence[1], 0) + get_letter(sequence[2], 0)
        world2 = letter + get_letter(sequence[1], 0) + get_letter(sequence[2], 1)


