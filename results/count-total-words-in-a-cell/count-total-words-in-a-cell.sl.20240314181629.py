def count_words(input_list):
    output_list = []
    for item in input_list:
        words = item[0].split()
        output_list.append(str(len(words)))
    return output_list

input_list = [['humpty dumpty'], ['humpty dumpty sat on a wall,'], ['couldnt put humpty together again.']]
output = count_words(input_list)
print(output)
