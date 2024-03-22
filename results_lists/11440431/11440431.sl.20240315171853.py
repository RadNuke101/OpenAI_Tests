def process_data(input_data):
    output = []
    for item in input_data:
        phrase = item[0]
        if phrase.isupper():
            processed_phrase = ' '.join(phrase.split()[:-1])
        else:
            processed_phrase = phrase
        output.append(processed_phrase)
    return output

input_data = [['Mining US'], ['Soybean Farming CAN'], ['Soybean Farming'], ['Oil Extraction US'], ['Fishing']]
output_data = process_data(input_data)
print(output_data)
