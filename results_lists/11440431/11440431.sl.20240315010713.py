def delete_last_phrase_if_all_caps(input_list):
    output_list = []
    for item in input_list:
        if item[0].isupper():
            output_list.append(item[0])
        else:
            output_list.append(item[0:-4].strip())
    return output_list

input_list = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
output = delete_last_phrase_if_all_caps(input_list)
print(output)
