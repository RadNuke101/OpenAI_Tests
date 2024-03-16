def remove_numbers(input_list):
    output_list = []
    for item in input_list:
        output_item = ''
        for char in item[0]:
            if not char.isdigit():
                output_item += char
        output_list.append(output_item)
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
output = remove_numbers(input_list)
print(output)
