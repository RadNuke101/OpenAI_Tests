def remove_numbers(input_list):
    output = []
    for sublist in input_list:
        for item in sublist:
            output.append(''.join([i for i in item if not i.isdigit()]))
    return output

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
