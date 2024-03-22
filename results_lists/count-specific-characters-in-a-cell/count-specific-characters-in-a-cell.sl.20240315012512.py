def count_letter_occurrences(input_list):
    output = []
    for pair in input_list:
        count = pair[0].count(pair[1])
        output.append(str(count))
    return output

input_list = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(input_list))
