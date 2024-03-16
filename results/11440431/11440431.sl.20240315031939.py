def process_input(input_list):
    output_list = []
    for item in input_list:
        if item[0].isupper():
            output_list.append(item[:-4])
        else:
            output_list.append(item[0])
    return output_list

input_list = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
output = process_input(input_list)
print(output)
