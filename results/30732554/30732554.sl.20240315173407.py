def clean_input(input_list):
    cleaned_list = []
    for item in input_list:
        if "|" in item[0]:
            cleaned_list.append(item[0].split("|")[0])
        else:
            cleaned_list.append(item[0])
    return cleaned_list

input_list = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
output = clean_input(input_list)
print(output)
