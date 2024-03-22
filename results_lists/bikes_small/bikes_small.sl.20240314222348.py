def get_text_before_last_three_numbers(input_list):
    output = []
    for item in input_list:
        text = ''.join([c for c in item[0] if not c.isdigit()])
        output.append(text)
    return output

input_list = [['Ducati100'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda550'], ['Ducati125']]
print(get_text_before_last_three_numbers(input_list))
