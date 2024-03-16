def clean_input(input_list):
    output_list = []
    for item in input_list:
        clean_item = item[0].split('|')[0] if '|' in item[0] else item[0]
        output_list.append(clean_item)
    return output_list

input_list = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
print(clean_input(input_list))
