def process_data(input_data):
    output = []
    for item in input_data:
        phrase = item[0]
        if phrase.isupper():
            output.append(phrase[:-1])
        else:
            output.append(phrase)
    return output

input_data = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
output_data = process_data(input_data)
print(output_data)
