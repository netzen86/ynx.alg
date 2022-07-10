def longest_word(wc, sentence):
    sentence = sentence.split()
    longest_word = []
    longest_word.append(sentence[0])
    longest_word.append(len(sentence[0]))
    for index in range(1, (len(sentence))):
        if len(sentence[index]) > longest_word[1]:
            longest_word = []
            longest_word.append(sentence[index])
            longest_word.append(len(sentence[index]))
    return longest_word


wc = input()
sentence = input()
lw = longest_word(wc, sentence)
print(f'{lw[0]}\n{lw[1]}')
