def clean_input(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            clean_item = item.split('|')[0].strip()
            output_list.append(clean_item)
    return output_list

input_list = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
output = clean_input(input_list)
print(output)
