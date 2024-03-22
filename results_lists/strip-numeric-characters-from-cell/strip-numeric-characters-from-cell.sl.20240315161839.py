def remove_numbers(input_list):
    output = []
    for sublist in input_list:
        output.append(''.join([i for i in sublist[0] if not i.isdigit()]))
    return output

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
output = remove_numbers(input_list)
print(output)
