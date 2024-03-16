def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(''.join([char for char in sublist[0] if not char.isdigit()]))
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
