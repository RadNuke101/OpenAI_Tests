def count_letter_occurrences(input_list):
    output = []
    for item in input_list:
        count = item[0].count(item[1])
        output.append(str(count))
    return output

input_list = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(input_list))
