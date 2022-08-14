def subsequence(string, substring):
    if len(set(string + substring)) == len(string):
        return True
    else:
        return False


if __name__ == '__main__':
    substring = input()
    string = input()
    print(subsequence(string, substring))
