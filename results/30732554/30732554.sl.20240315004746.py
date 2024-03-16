def clean_data(input_data):
    output_data = []
    for item in input_data:
        if "|" in item[0]:
            clean_item = item[0].split("|")[0]
            output_data.append(clean_item)
        else:
            output_data.append(item[0])
    return output_data

input_data = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
output = clean_data(input_data)
print(output)
