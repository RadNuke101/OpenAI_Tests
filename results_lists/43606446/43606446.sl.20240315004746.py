def get_capitalized_letters(input_list):
    output_list = []
    for item in input_list:
        expression = item[0]
        index = expression.find('>')
        letters = expression[index-3:index].upper()
        output_list.append(letters)
    return output_list

input_list = [['USD.EUR<IDEALPRO,CASH,EUR>'], ['USD.EUR<IDEALPRO,CASH,USD>'], ['KOR.JPN<IDEALPRO,CASH,WON>'], ['KOR.JPN<IDEALPRO,CASH,YEN>']]
output = get_capitalized_letters(input_list)
print(output)
