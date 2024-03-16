def process_input(input_list):
    output_list = []
    for sublist in input_list:
        phrase = sublist[0]
        if phrase.isupper():
            output_list.append(phrase[:-1])
        else:
            output_list.append(phrase)
    return output_list

input_list = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
output = process_input(input_list)
print(output)
