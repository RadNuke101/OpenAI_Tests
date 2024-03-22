def count_letter_appearance(input_list):
    output = []
    for expression, letter in input_list:
        count = expression.count(letter)
        output.append(str(count))
    return output

input_list = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_appearance(input_list))
