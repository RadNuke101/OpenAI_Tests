def get_text_before_last_three_numbers(input_list):
    output = []
    for item in input_list:
        text = item[0]
        for i in range(len(text) - 1, -1, -1):
            if text[i].isdigit():
                text = text[:i]
                break
        output.append(text)
    return output

input_list = [['Ducati100'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda550'], ['Ducati125']]
print(get_text_before_last_three_numbers(input_list))
