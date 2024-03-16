def clean_input(input_list):
    output_list = []
    for item in input_list:
        if "|" in item[0]:
            output_list.append(item[0].split("|")[0])
        else:
            output_list.append(item[0])
    return output_list

input_list = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
print(clean_input(input_list))
