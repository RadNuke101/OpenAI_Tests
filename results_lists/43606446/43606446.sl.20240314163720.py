def extract_capitalized_letters(data):
    output = []
    for item in data:
        expression = item[0]
        index = expression.find('>')
        letters = expression[index-3:index].split(',')
        for letter in letters:
            if letter.isupper():
                output.append(letter)
    return output

data = [['USD.EUR<IDEALPRO,CASH,EUR>'], ['USD.EUR<IDEALPRO,CASH,USD>'], ['KOR.JPN<IDEALPRO,CASH,WON>'], ['KOR.JPN<IDEALPRO,CASH,YEN>']]
output = extract_capitalized_letters(data)
print(output)
