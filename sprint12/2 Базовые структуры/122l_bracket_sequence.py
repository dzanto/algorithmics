brackets_dict = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def solution(bracket_seq):
    stack = []
    open_br = ['(', '{', '[']
    for bracket in bracket_seq:
        if bracket in open_br:
            stack.append(bracket)
        else:
            if bracket == brackets_dict[stack.pop()]:
                continue
            else:
                return False
    if stack == []:
        return True
    else:
        return False


if __name__ == "__main__":
    bracket_seq = list(input())
    print(solution(bracket_seq))
