def count_words(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        output.append(str(len(words)))
    return output

input_list = [['humpty dumpty'], ['humpty dumpty sat on a wall,'], ['couldnt put humpty together again.']]
output = count_words(input_list)
print(output)
