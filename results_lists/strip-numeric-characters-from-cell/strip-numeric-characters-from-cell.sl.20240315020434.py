def remove_numbers(input_list):
    output_list = []
    for item in input_list:
        new_item = ''.join([i for i in item[0] if not i.isdigit()])
        output_list.append(new_item)
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
