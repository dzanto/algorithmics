CALC = {
    '(': (lambda stack: stack.push),
    'peek': (lambda stack: stack.peek()),
    'size': (lambda stack: stack.size()),
}
def solution(bracket_seq):
    stack = []
    for bracket in bracket_seq:
        if bracket == '(' or '{' or '[':
            stack.append(bracket)
        else:
            stack.pop()


if __name__ == "__main__":
    bracket_seq = list(input())
    print(bracket_seq)
    solution(bracket_seq)