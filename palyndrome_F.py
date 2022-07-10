def palybdrome(sentence):
    sentence = ''.join(e for e in sentence if e.isalnum()).lower()
    return sentence == sentence[::-1]


sentence = input()

print(palybdrome(sentence))
