def count_letter_occurrences(input_list):
    output = []
    for item in input_list:
        expression = item[0]
        letter = item[1]
        count = expression.count(letter)
        output.append(str(count))
    return output

input_list = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(input_list))
