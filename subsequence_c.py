def subsequence(string, substring):
    position = 0
    for i in substring:
        position = string.find(i, position)
        position += 1
        if not position:
            return False
    return True


if __name__ == '__main__':
    substring = input()
    string = input()
    print(subsequence(string, substring))
