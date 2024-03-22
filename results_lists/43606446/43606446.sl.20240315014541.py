def get_capitalized_letters(data):
    output = []
    for item in data:
        letters = item[0].split('.')[1].split('<')[0][-3:].upper()
        output.append(letters)
    return output

input_data = [['USD.EUR<IDEALPRO,CASH,EUR>'], ['USD.EUR<IDEALPRO,CASH,USD>'], ['KOR.JPN<IDEALPRO,CASH,WON>'], ['KOR.JPN<IDEALPRO,CASH,YEN>']]
output_data = get_capitalized_letters(input_data)
print(output_data)
