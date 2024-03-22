def extract_text(input_list):
    output_list = []
    for item in input_list:
        text = item[0][:-3]
        output_list.append(text)
    return output_list

input_list = [['Ducati100'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda550'], ['Ducati125']]
print(extract_text(input_list))
