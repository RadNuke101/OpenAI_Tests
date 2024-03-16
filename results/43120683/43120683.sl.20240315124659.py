def process_input(input_list):
    output = []
    for item in input_list:
        first_word = item[0].split(',')[0]
        number = int(item[1].strip())
        if number == 1:
            output.append(first_word + ' apple')
        elif number == 2:
            output.append(first_word + ' bananas')
        elif number == 3:
            output.append(first_word + ' strawberries')
        elif number == 4:
            output.append(first_word + ' oranges')
    return output

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
