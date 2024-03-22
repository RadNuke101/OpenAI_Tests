def extract_text(input_list):
    output = []
    for item in input_list:
        text = item[0][:-3]
        output.append(text)
    return output

input_list = [['Ducati100'], ['Ducati100'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Ducati250'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura100'], ['Acura100'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati100'], ['Honda125'], ['Honda125'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda250'], ['Honda250'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Acura100'], ['Acura125'], ['Acura125'], ['Acura125'], ['Ferrari250'], ['Ferrari250'], ['Ferrari250'], ['Honda550'], ['Honda550'], ['Honda550'], ['Ducati125'], ['Ducati125'], ['Ducati125'], ['Ducati125']]
output = extract_text(input_list)
print(output)
