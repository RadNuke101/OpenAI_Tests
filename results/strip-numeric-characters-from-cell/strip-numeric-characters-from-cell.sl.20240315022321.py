def remove_numbers(input_list):
    output_list = []
    for item in input_list:
        output_list.append(''.join([i for i in item[0] if not i.isdigit()]))
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
