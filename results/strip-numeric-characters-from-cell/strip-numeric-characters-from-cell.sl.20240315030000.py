def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        output_sublist = ''
        for item in sublist:
            output_item = ''.join([char for char in item if not char.isdigit()])
            output_sublist += output_item
        output_list.append(output_sublist)
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
