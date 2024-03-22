def get_text_before_last_three_numbers(input_list):
    output_list = []
    for item in input_list:
        text = ''.join(filter(str.isalpha, item[0]))
        output_list.append(text)
    return output_list

input_list = [['Ducati100'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda550'], ['Ducati125']]
print(get_text_before_last_three_numbers(input_list))
