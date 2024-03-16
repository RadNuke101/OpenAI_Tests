def get_text_before_last_three_numbers(input_list):
    output_list = []
    for item in input_list:
        text = item[0][:-3]
        output_list.append(text)
    return output_list

input_list = [['Ducati100'], ['Ducati100'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Ducati250'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura100'], ['Acura100'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura125'], ['Acura125'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati125']]
print(get_text_before_last_three_numbers(input_list))
