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

text = []

def solution(seq, string):
    button = seq[0]
    if len(seq) == 1:
        for letter in buttons[button]:
            text.append(string + letter)
    else:
        for letter in buttons[button]:
            solution(seq[1::], string + letter)


if __name__ == '__main__':
    sequence = list(map(int, input()))
    solution(sequence, '')
    print(' '.join(text))
