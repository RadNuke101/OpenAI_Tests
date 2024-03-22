def count_letter_occurrences(input_list):
    output_list = []
    for input_pair in input_list:
        expression = input_pair[0]
        letter = input_pair[1]
        count = expression.count(letter)
        output_list.append(str(count))
    return output_list

input_list = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(input_list))
