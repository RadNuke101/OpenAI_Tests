def get_capitalized_letters(data):
    result = []
    for item in data:
        expression = item[0]
        index = expression.find('>')
        letters = expression[index-3:index].upper()
        result.append(letters)
    return result

input_data = [['USD.EUR<IDEALPRO,CASH,EUR>'], ['USD.EUR<IDEALPRO,CASH,USD>'], ['KOR.JPN<IDEALPRO,CASH,WON>'], ['KOR.JPN<IDEALPRO,CASH,YEN>']]
output = get_capitalized_letters(input_data)
print(output)
