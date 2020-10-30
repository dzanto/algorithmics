brackets_dict = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def solution(bracket_seq):
    stack = []
    for bracket in bracket_seq:
        if bracket in brackets_dict:
            stack.append(bracket)
        else:
            if stack == []:
                return False
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
