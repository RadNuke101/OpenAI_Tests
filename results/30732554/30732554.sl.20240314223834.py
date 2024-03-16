def process_input(input_data):
    output = []
    for item in input_data:
        if "|" in item[0]:
            output.append(item[0].split("|")[0])
        else:
            output.append(item[0])
    return output

input_data = [['TL-18273982| 10MM'], ['TL-288762| 76DK'], ['CT-576'], ['N/A']]
print(process_input(input_data))
