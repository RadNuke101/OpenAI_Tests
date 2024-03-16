def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        new_sublist = []
        for item in sublist:
            new_item = ''.join([i for i in item if not i.isdigit()])
            new_sublist.append(new_item)
        output_list.append(''.join(new_sublist))
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
output = remove_numbers(input_list)
print(output)
