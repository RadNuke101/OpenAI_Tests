def count_words(expressions):
    result = []
    for exp in expressions:
        words = exp[0].split()
        result.append(str(len(words)))
    return result

input_data = [['humpty dumpty'], ['humpty dumpty sat on a wall,'], ['couldnt put humpty together again.']]
output_data = count_words(input_data)
print(output_data)
