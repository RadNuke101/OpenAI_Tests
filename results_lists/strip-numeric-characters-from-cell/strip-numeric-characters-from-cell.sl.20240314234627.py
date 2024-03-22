def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        output = ''
        for item in sublist:
            output += ''.join([char for char in item if not char.isdigit()])
        output_list.append(output)
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
