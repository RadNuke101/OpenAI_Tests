def get_capitalized_letters(data):
    result = []
    for item in data:
        letters = item[0].split('.')[1].split('<')[0]
        result.append(letters.upper())
    return result

input_data = [['USD.EUR<IDEALPRO,CASH,EUR>'], ['USD.EUR<IDEALPRO,CASH,USD>'], ['KOR.JPN<IDEALPRO,CASH,WON>'], ['KOR.JPN<IDEALPRO,CASH,YEN>']]
output = get_capitalized_letters(input_data)
print(output)
