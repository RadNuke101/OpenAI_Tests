def get_text_before_last_three_numbers(input_list):
    result = []
    for item in input_list:
        text = item[0]
        for i in range(len(text)-1, -1, -1):
            if text[i].isdigit():
                if text[i-1].isdigit() and text[i-2].isdigit():
                    result.append(text[:i-2])
                    break
    return result

input_list = [['Ducati100'], ['Honda125'], ['Ducati250'], ['Honda250'], ['Honda550'], ['Ducati125']]
output = get_text_before_last_three_numbers(input_list)
print(output)
