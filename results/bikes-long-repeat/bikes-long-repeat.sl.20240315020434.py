def extract_text_before_last_three_numbers(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        index = len(text) - 1
        count = 0
        while index >= 0 and count < 3:
            if text[index].isdigit():
                count += 1
            index -= 1
        output_list.append(text[:index + 2])
    return output_list

input_list = [['Ducati100'], ['Ducati100'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Ducati250'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura100'], ['Acura100'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura125'], ['Acura125'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati125']]
print(extract_text_before_last_three_numbers(input_list))
