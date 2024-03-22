def check_number_presence(input_list):
    output_list = []
    for expression in input_list:
        if any(char.isdigit() for char in expression[0]):
            output_list.append('true')
        else:
            output_list.append('false')
    return output_list

input_list = [['A bird in the hand is worth 2 in the bush.'], ['A bird in the hand is worth two in the bush.'], ['The 15 shortcuts you simply must know']]
output = check_number_presence(input_list)
print(output)
