def replace_chars(input_list):
    output_list = []
    for item in input_list:
        new_item = item[0].replace('<', ' ').replace('>', ' ').replace(',', ' ')
        output_list.append(new_item)
    return output_list

input_list = [['R/V<208,0,32>'], ['R/S<184,28,16>'], ['R/B<255,88,80>']]
output = replace_chars(input_list)
print(output)
