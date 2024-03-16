def process_data(input_data):
    output = []
    for item in input_data:
        if item[0].isupper():
            output.append(item[0].rsplit(' ', 1)[0])
        else:
            output.append(item[0])
    return output

input_data = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
print(process_data(input_data))
