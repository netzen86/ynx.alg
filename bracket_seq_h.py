
def is_correct_bracket_seq(seq):
    stack = []
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for bracket in seq:
        if bracket in ['(', '{', '[']:
            stack.append(bracket)
        elif bracket in [')', '}', ']']:
            if not stack:
                return False
            popped = stack.pop()
            if brackets[popped] != bracket:
                return False
    return stack == []

if __name__ == '__main__':
    seq = input()
    print(is_correct_bracket_seq(seq))
