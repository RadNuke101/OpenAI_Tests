def remove_numbers(input_list):
    output = []
    for item in input_list:
        output.append(''.join([char for char in item[0] if not char.isdigit()]))
    return output

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
