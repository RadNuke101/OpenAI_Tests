def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        output_sublist = ' '.join([word for word in sublist[0].split() if not word.isdigit()])
        output_list.append(output_sublist)
    return output_list

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
output = remove_numbers(input_list)
print(output)
