def remove_numbers(input_list):
    output = []
    for sublist in input_list:
        text = ' '.join(sublist)
        text_without_numbers = ''.join([i for i in text if not i.isdigit()])
        output.append(text_without_numbers)
    return output

input_list = [['34653 jim mcdonald'], ['price is 500'], ['100 apples']]
print(remove_numbers(input_list))
