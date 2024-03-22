def count_words(input_list):
    output = []
    for words in input_list:
        word_count = len(words[0].split())
        output.append(str(word_count))
    return output

input_list = [['humpty dumpty'], ['humpty dumpty sat on a wall,'], ['couldnt put humpty together again.']]
print(count_words(input_list))
