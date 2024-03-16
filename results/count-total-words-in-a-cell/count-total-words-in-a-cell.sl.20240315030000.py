def count_words(input_data):
    output = []
    for item in input_data:
        words = item[0].split()
        output.append(str(len(words)))
    return output

input_data = [['humpty dumpty'], ['humpty dumpty sat on a wall,'], ['couldnt put humpty together again.']]
print(count_words(input_data))
