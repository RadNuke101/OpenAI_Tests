def process_input(input_list):
    output = []
    for item in input_list:
        word = item[0].split(',')[0]
        num = int(item[1])
        if num == 1:
            output.append(word + ' apple')
        elif num == 2:
            output.append(word + ' bananas')
        elif num == 3:
            output.append(word + ' strawberries')
        elif num == 4:
            output.append(word + ' oranges')
    return output

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
