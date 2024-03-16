def remove_numbers(input_list):
    output = []
    for sublist in input_list:
        text = ' '.join(filter(lambda x: not x.isdigit(), sublist[0].split()))
        output.append(text)
    return output

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
