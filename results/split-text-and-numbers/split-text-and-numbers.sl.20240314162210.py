def remove_numbers(input_list):
    output_list = []
    for pair in input_list:
        word = ''.join([char for char in pair[0] if not char.isdigit()])
        output_list.append(word)
    return output_list

input_list = [['apples30', '7'], ['peaches24', '8'], ['peaches0', '8'], ['pears', '6']]
print(remove_numbers(input_list))
